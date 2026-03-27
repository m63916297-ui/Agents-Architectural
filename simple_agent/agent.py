import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()


class SimpleAgent:
    """
    Simple Single-Agent Architecture

    Este agente implementa la arquitectura mas basica de un agente de IA,
    siguiendo el patron de Agentes de LangChain con entrada/salida simple.
    """

    def __init__(self, model_name: str = "gpt-4", temperature: float = 0.7):
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)
        self.system_prompt = """Eres un asistente de IA util, respetuoso y honesto.
Responde de manera clara, concisa y util a las preguntas del usuario."""

    def chat(self, user_input: str) -> str:
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=user_input),
        ]
        response = self.llm.invoke(messages)
        return response.content

    def run(self, user_input: str) -> str:
        return self.chat(user_input)


if __name__ == "__main__":
    agent = SimpleAgent()
    print("Simple Agent - Escribe 'salir' para terminar")
    while True:
        user_input = input("\nTu: ")
        if user_input.lower() == "salir":
            break
        print("\nAgente:", agent.run(user_input))
