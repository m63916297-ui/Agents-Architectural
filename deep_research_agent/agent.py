import os
import requests
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from typing import List, Dict

load_dotenv()


class DeepResearchAgent:
    """
    Deep Research Agent - Arquitectura de Investigación Profunda

    Este agente implementa capacidades de investigación profunda con
    iteración, verificación y síntesis de información de múltiples fuentes.

    Arquitectura:
    ┌─────────────────┐
    │  User Query      │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │   QUERY PLAN     │◄──── Descomposición
    │   (Planificación) │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │   ITERATIVE      │
    │   RESEARCH       │◄──── Múltiples fuentes
    │   (Iterativo)    │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │   VERIFICATION   │◄──── Auto-verificación
    │   (Verificación) │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │   SYNTHESIS      │◄──── LLM
    │   (Síntesis)    │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │   DEEP REPORT    │
    └─────────────────┘
    """

    def __init__(self, model_name: str = "gpt-4", temperature: float = 0.2):
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            streaming=True,
            callbacks=[StreamingStdOutCallbackHandler()],
        )

        self.system_prompt = """Eres un investigador académico de alto nivel.
Tu rol es realizar investigación profunda siguiendo metodologías rigurosas.

Metodología:
1. PLANIFICAR: Descomponer la consulta en subtemas
2. INVESTIGAR: Buscar en múltiples fuentes de forma iterativa
3. VERIFICAR: Cruzar información y validar fuentes
4. SINTETIZAR: Integrar conocimientos en un reporte coherente

Estándar académico: precisión, objetividad, citas apropiadas."""

    def plan_query(self, query: str) -> List[str]:
        """Planifica la investigación descompiendo la consulta"""
        planning_prompt = f"""Analiza esta consulta de investigación y descompónla en subtemas específicos:

Consulta: {query}

Subtemas a investigar (lista separada por comas):"""

        messages = [
            SystemMessage(content="Eres un planificador de investigación."),
            HumanMessage(content=planning_prompt),
        ]

        response = self.llm.invoke(messages).content
        subtemas = [s.strip() for s in response.split(",")]
        return subtemas[:5]

    def search_wikipedia(self, query: str) -> List[Dict]:
        """Busca en Wikipedia"""
        try:
            url = f"https://en.wikipedia.org/w/api.php"
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
        except:
            return []

    def verify_information(self, information: str, topic: str) -> str:
        """Verifica y valida la información"""
        verify_prompt = f"""Verifica la siguiente información sobre {topic}:

{information}

Indica:
1. ¿Es coherente y lógica?
2. ¿Hay inconsistencias?
3. ¿Qué puntos necesitan más investigación?

Verificación:"""

        messages = [
            SystemMessage(content="Eres un verificador de información."),
            HumanMessage(content=verify_prompt),
        ]

        return self.llm.invoke(messages).content

    def synthesize_deep_report(
        self, topic: str, research_data: List[str], verifications: List[str]
    ) -> str:
        """Sintetiza un reporte de investigación profunda"""
        synthesis_prompt = f"""Genera un reporte de investigación profunda sobre: {topic}

Datos recopilados:
{chr(10).join(research_data)}

Verificaciones:
{chr(10).join(verifications)}

Estructura del reporte:
1. RESUMEN EJECUTIVO (200 palabras)
2. INTRODUCCIÓN Y CONTEXTO
3. ANÁLISIS DETALLADO
   3.1 Subtema 1
   3.2 Subtema 2
   3.3 Subtema 3
4. HALLAZGOS PRINCIPALES
5. DISCUSIÓN Y ANÁLISIS CRÍTICO
6. LIMITACIONES
7. CONCLUSIONES
8. RECOMENDACIONES
9. FUENTES Y CITAS

El reporte debe ser comprehensivo y demostrar investigación rigurosa."""

        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=synthesis_prompt),
        ]

        return self.llm.invoke(messages).content

    def deep_research(self, query: str) -> Dict:
        """Ejecuta investigación profunda completa"""
        results = {
            "query": query,
            "subtopics": [],
            "research_data": [],
            "verifications": [],
            "report": "",
        }

        with st_spinner("Planificando investigación..."):
            results["subtopics"] = self.plan_query(query)

        with st_spinner("Investigando..."):
            for subtema in results["subtopics"]:
                data = self.search_wikipedia(subtema)
                if data:
                    results["research_data"].extend(data)

        with st_spinner("Verificando información..."):
            research_text = "\n".join(
                [
                    f"- {d['title']}: {d.get('snippet', '')}"
                    for d in results["research_data"]
                ]
            )
            results["verifications"].append(
                self.verify_information(research_text, query)
            )

        with st_spinner("Sintetizando reporte..."):
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


def st_spinner(text):
    class SpinnerContext:
        def __enter__(self):
            print(f"[INFO] {text}")
            return self

        def __exit__(self, *args):
            pass

    return SpinnerContext()


if __name__ == "__main__":
    agent = DeepResearchAgent()
    print("Deep Research Agent - Investigación profunda automatizada")
    print("Escribe 'salir' para terminar\n")

    while True:
        query = input("\nConsulta de investigación: ")
        if query.lower() == "salir":
            break

        results = agent.deep_research(query)

        print("\n" + "=" * 50)
        print("REPORTE DE INVESTIGACIÓN PROFUNDA")
        print("=" * 50)
        print(results["report"])
