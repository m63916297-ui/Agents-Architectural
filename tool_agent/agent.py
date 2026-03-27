import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import Tool
from langchain.schema import HumanMessage, SystemMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from typing import List

load_dotenv()


def get_current_time() -> str:
    """Obtiene la fecha y hora actual"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def search_wikipedia(query: str) -> str:
    """Busca información en Wikipedia"""
    try:
        url = f"https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
        }
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if data.get("query", {}).get("search"):
            results = data["query"]["search"][:3]
            return "\n".join(
                [f"- {r['title']}: {r['snippet'][:200]}..." for r in results]
            )
        return "No se encontraron resultados."
    except Exception as e:
        return f"Error en búsqueda: {str(e)}"


def calculate(expression: str) -> str:
    """Calcula expresiones matemáticas"""
    try:
        result = eval(expression)
        return f"El resultado de {expression} es {result}"
    except Exception as e:
        return f"Error en cálculo: {str(e)}"


class ToolAgent:
    """
    Tool Agent - Arquitectura con Uso de Herramientas

    Este agente implementa el patrón ReAct (Reasoning + Acting)
    utilizando herramientas externas para completar tareas.

    Arquitectura:
    ┌─────────────────┐
    │  User Input      │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │    THOUGHTS      │◄──── ¿Qué necesito hacer?
    │  (Razonamiento) │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │    ACTIONS       │◄──── Elegir herramienta
    │  (Herramientas)  │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │    OBSERVATIONS  │◄──── Resultado de herramienta
    │  (Observaciones) │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │    LLM (GPT-4)   │◄──── Procesar ciclo ReAct
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │    Response      │
    └─────────────────┘
    """

    def __init__(self, model_name: str = "gpt-4", temperature: float = 0.3):
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            streaming=True,
            callbacks=[StreamingStdOutCallbackHandler()],
        )

        self.tools = [
            Tool(
                name="Tiempo Actual",
                func=lambda x: get_current_time(),
                description="Útil para obtener la fecha y hora actual del sistema",
            ),
            Tool(
                name="Buscar Wikipedia",
                func=search_wikipedia,
                description="Útil para buscar información general en Wikipedia. Entrada: término de búsqueda",
            ),
            Tool(
                name="Calculadora",
                func=calculate,
                description="Útil para realizar cálculos matemáticos. Entrada: expresión matemática",
            ),
        ]

        self.system_prompt = """Eres un asistente de IA con acceso a herramientas externas.

Herramientas disponibles:
- Tiempo Actual: Obtiene fecha y hora actual
- Buscar Wikipedia: Busca información general
- Calculadora: Realiza cálculos matemáticos

Metodología ReAct:
1. THOUGHT: Piensa qué necesitas hacer
2. ACTION: Usa una herramienta si es necesario
3. OBSERVATION: Analiza el resultado
4. RESPONSE: Responde al usuario

Si no necesitas herramientas, responde directamente."""

    def chat(self, user_input: str) -> str:
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=user_input),
        ]

        for tool in self.tools:
            messages.append(HumanMessage(content=f"[{tool.name}]: {tool.description}"))

        response = self.llm.invoke(messages)
        return response.content

    def run(self, user_input: str) -> str:
        return self.chat(user_input)


if __name__ == "__main__":
    agent = ToolAgent()
    print("Tool Agent - Agente con herramientas (ReAct)")
    print("Herramientas: tiempo, wikipedia, calculadora")
    print("Escribe 'salir' para terminar\n")

    while True:
        user_input = input("\nTú: ")
        if user_input.lower() == "salir":
            break
        print("\nAgente: ", end="")
        agent.run(user_input)
