import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.tools import Tool

load_dotenv()


def get_current_time() -> str:
    """Obtiene la fecha y hora actual"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def search_wikipedia(query: str) -> str:
    """Busca informacion en Wikipedia"""
    try:
        url = "https://en.wikipedia.org/w/api.php"
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
        return f"Error en busqueda: {str(e)}"


def calculate(expression: str) -> str:
    """Calcula expresiones matematicas"""
    try:
        result = eval(expression)
        return f"El resultado de {expression} es {result}"
    except Exception as e:
        return f"Error en calculo: {str(e)}"


class ToolAgent:
    """
    Tool Agent - Arquitectura con Uso de Herramientas

    Este agente implementa el patron ReAct (Reasoning + Acting)
    utilizando herramientas externas para completar tareas.
    """

    def __init__(self, model_name: str = "gpt-4", temperature: float = 0.3):
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)

        self.tools = [
            Tool(
                name="Tiempo Actual",
                func=lambda x: get_current_time(),
                description="Utill para obtener la fecha y hora actual del sistema",
            ),
            Tool(
                name="Buscar Wikipedia",
                func=search_wikipedia,
                description="Util para buscar informacion general en Wikipedia. Entrada: termino de busqueda",
            ),
            Tool(
                name="Calculadora",
                func=calculate,
                description="Util para realizar calculos matematicos. Entrada: expresion matematica",
            ),
        ]

        self.system_prompt = """Eres un asistente de IA con acceso a herramientas externas.

Herramientas disponibles:
- Tiempo Actual: Obtiene fecha y hora actual
- Buscar Wikipedia: Busca informacion general
- Calculadora: Realiza calculos matematicos

Si no necesitas herramientas, responde directamente."""

    def chat(self, user_input: str) -> str:
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(
                content=f"Herramientas disponibles: {[t.name for t in self.tools]}"
            ),
            HumanMessage(content=user_input),
        ]

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
        user_input = input("\nTu: ")
        if user_input.lower() == "salir":
            break
        print("\nAgente:", agent.run(user_input))
