import os
import requests
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from typing import List, Dict

load_dotenv()


class SimpleSpinner:
    """Context manager simple para spinners en terminal"""

    def __init__(self, text):
        self.text = text

    def __enter__(self):
        print(f"[INFO] {self.text}")
        return self

    def __exit__(self, *args):
        pass


class DeepResearchAgent:
    """
    Deep Research Agent - Arquitectura de Investigacion Profunda

    Este agente implementa capacidades de investigacion profunda con
    iteracion, verificacion y sintesis de informacion de multiples fuentes.
    """

    def __init__(self, model_name: str = "gpt-4", temperature: float = 0.2):
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            streaming=True,
            callbacks=[StreamingStdOutCallbackHandler()],
        )

        self.system_prompt = """Eres un investigador academico de alto nivel.
Tu rol es realizar investigacion profunda siguiendo metodologias rigurosas.

Metodologia:
1. PLANIFICAR: Descomponer la consulta en subtemas
2. INVESTIGAR: Buscar en multiples fuentes de forma iterativa
3. VERIFICAR: Cruzar informacion y validar fuentes
4. SINTETIZAR: Integrar conocimientos en un reporte coherente

Estandar academico: precision, objetividad, citas apropiadas."""

    def plan_query(self, query: str) -> List[str]:
        """Planifica la investigacion descomponiendo la consulta"""
        planning_prompt = f"""Analiza esta consulta de investigacion y descompongla en subtemas especificos:

Consulta: {query}

Subtemas a investigar (lista separada por comas):"""

        messages = [
            SystemMessage(content="Eres un planificador de investigacion."),
            HumanMessage(content=planning_prompt),
        ]

        response = self.llm.invoke(messages).content
        subtemas = [s.strip() for s in response.split(",")]
        return subtemas[:5]

    def search_wikipedia(self, query: str) -> List[Dict]:
        """Busca en Wikipedia"""
        try:
            url = "https://en.wikipedia.org/w/api.php"
            params = {
                "action": "query",
                "list": "search",
                "srsearch": query,
                "format": "json",
                "srlimit": 3,
            }
            response = requests.get(url, params=params, timeout=10)
            data = response.json()

            results = []
            for item in data.get("query", {}).get("search", []):
                results.append(
                    {
                        "title": item["title"],
                        "snippet": item["snippet"],
                        "source": "Wikipedia",
                    }
                )
            return results
        except Exception:
            return []

    def verify_information(self, information: str, topic: str) -> str:
        """Verifica y valida la informacion"""
        verify_prompt = f"""Verifica la siguiente informacion sobre {topic}:

{information}

Indica:
1. Es coherente y logica?
2. Hay inconsistencias?
3. Que puntos necesitan mas investigacion?

Verificacion:"""

        messages = [
            SystemMessage(content="Eres un verificador de informacion."),
            HumanMessage(content=verify_prompt),
        ]

        return self.llm.invoke(messages).content

    def synthesize_deep_report(
        self, topic: str, research_data: List[str], verifications: List[str]
    ) -> str:
        """Sintetiza un reporte de investigacion profunda"""
        synthesis_prompt = f"""Genera un reporte de investigacion profunda sobre: {topic}

Datos recopilados:
{chr(10).join(research_data)}

Verificaciones:
{chr(10).join(verifications)}

Estructura del reporte:
1. RESUMEN EJECUTIVO (200 palabras)
2. INTRODUCCION Y CONTEXTO
3. ANALISIS DETALLADO
   3.1 Subtema 1
   3.2 Subtema 2
   3.3 Subtema 3
4. HALLAZGOS PRINCIPALES
5. DISCUSION Y ANALISIS CRITICO
6. LIMITACIONES
7. CONCLUSIONES
8. RECOMENDACIONES
9. FUENTES Y CITAS

El reporte debe ser comprehensivo y demostrar investigacion rigurosa."""

        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=synthesis_prompt),
        ]

        return self.llm.invoke(messages).content

    def deep_research(self, query: str) -> Dict:
        """Ejecuta investigacion profunda completa"""
        results = {
            "query": query,
            "subtopics": [],
            "research_data": [],
            "verifications": [],
            "report": "",
        }

        with SimpleSpinner("Planificando investigacion..."):
            results["subtopics"] = self.plan_query(query)

        with SimpleSpinner("Investigando..."):
            for subtema in results["subtopics"]:
                data = self.search_wikipedia(subtema)
                if data:
                    results["research_data"].extend(data)

        with SimpleSpinner("Verificando informacion..."):
            research_text = "\n".join(
                [
                    f"- {d['title']}: {d.get('snippet', '')}"
                    for d in results["research_data"]
                ]
            )
            results["verifications"].append(
                self.verify_information(research_text, query)
            )

        with SimpleSpinner("Sintetizando reporte..."):
            results["report"] = self.synthesize_deep_report(
                query,
                [
                    f"{d['title']}: {d.get('snippet', '')}"
                    for d in results["research_data"]
                ],
                results["verifications"],
            )

        return results

    def run(self, query: str) -> Dict:
        return self.deep_research(query)


if __name__ == "__main__":
    agent = DeepResearchAgent()
    print("Deep Research Agent - Investigacion profunda automatizada")
    print("Escribe 'salir' para terminar\n")

    while True:
        query = input("\nConsulta de investigacion: ")
        if query.lower() == "salir":
            break

        results = agent.deep_research(query)

        print("\n" + "=" * 50)
        print("REPORTE DE INVESTIGACION PROFUNDA")
        print("=" * 50)
        print(results["report"])
