import os
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


class ResearchAgent:
    """Agente especializado en investigacion"""

    def __init__(self, llm):
        self.llm = llm
        self.role = "Investigador"
        self.prompt = """Eres un investigador experto. Tu rol es:
- Buscar y analizar informacion
- Identificar fuentes relevantes
- Proporcionar datos y hechos verificados
- Citar cuando sea posible

Responde de manera precisa y fundamentada."""

    def process(self, query: str) -> str:
        messages = [SystemMessage(content=self.prompt), HumanMessage(content=query)]
        return self.llm.invoke(messages).content


class AnalysisAgent:
    """Agente especializado en analisis"""

    def __init__(self, llm):
        self.llm = llm
        self.role = "Analista"
        self.prompt = """Eres un analista experto. Tu rol es:
- Analizar datos y informacion
- Identificar patrones y tendencias
- Comparar alternativas
- Evaluar pros y contras
- Sugerir mejoras

Se critico y objetivo en tu analisis."""

    def process(self, query: str) -> str:
        messages = [SystemMessage(content=self.prompt), HumanMessage(content=query)]
        return self.llm.invoke(messages).content


class CreativeAgent:
    """Agente especializado en creatividad"""

    def __init__(self, llm):
        self.llm = llm
        self.role = "Creativo"
        self.prompt = """Eres un experto en creatividad. Tu rol es:
- Generar ideas innovadoras
- Proponer soluciones creativas
- Explorar posibilidades no convencionales
- Estimular la reflexion
- Encontrar conexiones inesperadas

Se imaginativo y propositivo."""

    def process(self, query: str) -> str:
        messages = [SystemMessage(content=self.prompt), HumanMessage(content=query)]
        return self.llm.invoke(messages).content


class MultiAgentSystem:
    """
    Multi-Agent System - Arquitectura Colaborativa

    Este sistema implementa multiples agentes especializados que
    colaboran para resolver problemas complejos.
    """

    def __init__(self, model_name: str = "gpt-4", temperature: float = 0.7):
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            streaming=True,
            callbacks=[StreamingStdOutCallbackHandler()],
        )

        self.researcher = ResearchAgent(self.llm)
        self.analyst = AnalysisAgent(self.llm)
        self.creative = CreativeAgent(self.llm)

        self.system_prompt = """Eres el orquestador de un sistema multi-agente.
Coordinas a investigadores, analistas y creativos para resolver problemas."""

    def collaborate(self, query: str, use_all_agents: bool = True) -> Dict:
        """Ejecuta colaboracion entre agentes"""
        results = {"query": query, "agents": {}}

        if use_all_agents:
            with SimpleSpinner("Investigador trabajando..."):
                results["agents"]["researcher"] = self.researcher.process(query)

            with SimpleSpinner("Analista trabajando..."):
                results["agents"]["analyst"] = self.analyst.process(query)

            with SimpleSpinner("Creativo trabajando..."):
                combined = f"Basado en investigacion y analisis, genera ideas innovadoras:\n\nInvestigacion: {results['agents']['researcher'][:500]}\nAnalisis: {results['agents']['analyst'][:500]}"
                results["agents"]["creative"] = self.creative.process(combined)
        else:
            results["agents"]["researcher"] = self.researcher.process(query)

        synthesis_prompt = f"""Combina los resultados de los agentes en una respuesta coherente:

Investigacion: {results["agents"]["researcher"][:1000]}
Analisis: {results["agents"].get("analyst", "N/A")[:1000]}
Ideas Creativas: {results["agents"].get("creative", "N/A")[:1000]}

Proporciona una respuesta final integrada:"""

        results["synthesis"] = self.llm.invoke(
            [
                SystemMessage(content="Eres un sintetizador de informacion."),
                HumanMessage(content=synthesis_prompt),
            ]
        ).content

        return results

    def run(self, query: str, use_all_agents: bool = True) -> Dict:
        return self.collaborate(query, use_all_agents)


if __name__ == "__main__":
    system = MultiAgentSystem()
    print("Multi-Agent System - Sistema de agentes colaborativos")
    print("Escribe 'salir' para terminar\n")

    while True:
        query = input("\nConsulta: ")
        if query.lower() == "salir":
            break

        results = system.run(query, use_all_agents=True)

        print("\n=== RESULTADOS ===")
        print(f"\n[INVESTIGADOR]: {results['agents']['researcher'][:500]}")
        print(f"\n[ANALISTA]: {results['agents']['analyst'][:500]}")
        print(f"\n[CREADOR]: {results['agents']['creative'][:500]}")
        print(f"\n[SINTESIS]: {results['synthesis'][:500]}")
