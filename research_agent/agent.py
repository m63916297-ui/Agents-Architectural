import os
import requests
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()


class ResearchAgent:
    """
    Research Agent - Arquitectura de Agente de Investigacion

    Este agente implementa capacidades de busqueda y sintesis de informacion
    para investigacion academica y analisis profundo.
    """

    def __init__(self, model_name: str = "gpt-4", temperature: float = 0.3):
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)

        self.system_prompt = """Eres un asistente de investigacion experto.
Tu rol es:
- Buscar informacion relevante de multiples fuentes
- Analizar y sintetizar datos
- Proporcionar un reporte estructurado con citas
- Mantener objetividad y precision

Formato del reporte:
1. RESUMEN EJECUTIVO
2. ANTECEDENTES
3. HALLAZGOS PRINCIPALES
4. ANALISIS
5. CONCLUSIONES
6. FUENTES"""

    def search_wikipedia(self, query: str) -> list:
        """Busca en Wikipedia"""
        try:
            url = "https://en.wikipedia.org/w/api.php"
            params = {
                "action": "query",
                "list": "search",
                "srsearch": query,
                "format": "json",
                "srlimit": 5,
            }
            response = requests.get(url, params=params, timeout=10)
            data = response.json()

            results = []
            for item in data.get("query", {}).get("search", []):
                results.append(
                    {
                        "title": item["title"],
                        "snippet": item["snippet"],
                        "url": f"https://en.wikipedia.org/wiki/{item['title'].replace(' ', '_')}",
                    }
                )
            return results
        except Exception as e:
            return [{"error": str(e)}]

    def synthesize_information(self, topic: str, sources_data: list) -> str:
        """Sintetiza informacion de multiples fuentes"""
        synthesis_prompt = f"""Tema: {topic}

Informacion recopilada:
{chr(10).join(sources_data)}

Genera un reporte de investigacion estructurado siguiendo el formato estandar."""

        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=synthesis_prompt),
        ]

        return self.llm.invoke(messages).content

    def research(self, topic: str, deep: bool = False) -> dict:
        """Ejecuta investigacion completa"""
        results = {"topic": topic, "sources": [], "report": ""}

        wiki_results = self.search_wikipedia(topic)
        results["sources"].extend(wiki_results)

        sources_text = [
            f"- {s['title']}: {s.get('snippet', 'N/A')}" for s in wiki_results[:3]
        ]

        results["report"] = self.synthesize_information(topic, sources_text)

        return results

    def run(self, topic: str, deep: bool = False) -> dict:
        return self.research(topic, deep)


if __name__ == "__main__":
    agent = ResearchAgent()
    print("Research Agent - Agente de Investigacion")
    print("Escribe 'salir' para terminar\n")

    while True:
        topic = input("\nTema de investigacion: ")
        if topic.lower() == "salir":
            break

        results = agent.research(topic)

        print("\n=== REPORTE DE INVESTIGACION ===")
        print(results["report"])
        print("\n--- FUENTES ---")
        for src in results["sources"]:
            print(f"- {src['title']}")
