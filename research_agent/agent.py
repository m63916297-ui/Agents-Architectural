import os
import requests
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts import PromptTemplate
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from typing import List, Dict

load_dotenv()


class ResearchAgent:
    """
    Research Agent - Arquitectura de Agente de Investigación

    Este agente implementa capacidades de búsqueda y síntesis de información
    para investigación académica y análisis profundo.

    Arquitectura:
    ┌─────────────────┐
    │  Topic/Query     │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │   WEB SEARCH      │◄──── SerpAPI / Wikipedia
    │   (Búsqueda)      │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │   WEB SCRAPER    │◄──── BeautifulSoup
    │   (Extracción)   │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │   INFORMATION    │
    │   PROCESSING     │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │   SYNTHESIS      │◄──── LLM
    │   (Síntesis)     │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │   RESEARCH       │
    │   REPORT        │
    └─────────────────┘
    """

    def __init__(self, model_name: str = "gpt-4", temperature: float = 0.3):
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            streaming=True,
            callbacks=[StreamingStdOutCallbackHandler()],
        )

        self.system_prompt = """Eres un asistente de investigación experto.
Tu rol es:
- Buscar información relevante de múltiples fuentes
- Analizar y sintetizar datos
- Proporcionar un reporte estructurado con citas
- Mantener objectivity y precisión

Formato del reporte:
1. RESUMEN EJECUTIVO
2. ANTECEDENTES
3. HALLAZGOS PRINCIPALES
4. ANÁLISIS
5. CONCLUSIONES
6. FUENTES"""

    def search_wikipedia(self, query: str) -> List[Dict]:
        """Busca en Wikipedia"""
        try:
            url = f"https://en.wikipedia.org/w/api.php"
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

    def search_news(self, query: str) -> List[Dict]:
        """Busca noticias recientes (simulado)"""
        return [
            {
                "title": f"Noticia sobre {query}",
                "source": "NewsAPI",
                "date": "2026-03-27",
            }
        ]

    def synthesize_information(self, topic: str, sources_data: List[str]) -> str:
        """Sintetiza información de múltiples fuentes"""
        synthesis_prompt = f"""Tema: {topic}

Información recopilada:
{chr(10).join(sources_data)}

Genera un reporte de investigación estructurado siguiendo el formato estándar."""

        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=synthesis_prompt),
        ]

        return self.llm.invoke(messages).content

    def research(self, topic: str, deep: bool = False) -> Dict:
        """Ejecuta investigación completa"""
        results = {"topic": topic, "sources": [], "report": ""}

        wiki_results = self.search_wikipedia(topic)
        results["sources"].extend(wiki_results)

        sources_text = [
            f"- {s['title']}: {s.get('snippet', 'N/A')}" for s in wiki_results[:3]
        ]

        results["report"] = self.synthesize_information(topic, sources_text)

        return results

    def run(self, topic: str, deep: bool = False) -> Dict:
        return self.research(topic, deep)


if __name__ == "__main__":
    agent = ResearchAgent()
    print("Research Agent - Agente de Investigación")
    print("Escribe 'salir' para terminar\n")

    while True:
        topic = input("\nTema de investigación: ")
        if topic.lower() == "salir":
            break

        results = agent.research(topic)

        print("\n=== REPORTE DE INVESTIGACIÓN ===")
        print(results["report"])
        print("\n--- FUENTES ---")
        for src in results["sources"]:
            print(f"- {src['title']}")
