import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

load_dotenv()


class SimpleAgent:
    """
    Simple Single-Agent Architecture

    Este agente implementa la arquitectura más básica de un agente de IA,
    siguiendo el patrón de Agentes de LangChain con entrada/salida simple.

    Arquitectura:
    ┌─────────────────┐
    │   User Input    │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │   LLM (GPT-4)   │◄──── System Prompt
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │   Response      │
    └─────────────────┘
    """

    def __init__(self, model_name: str = "gpt-4", temperature: float = 0.7):
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            streaming=True,
            callbacks=[StreamingStdOutCallbackHandler()],
        )
        self.system_prompt = """Eres un asistente de IA útil, respetuoso y honesto.
Responde de manera clara, concisa y útil a las preguntas del usuario."""

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
        user_input = input("\nTú: ")
        if user_input.lower() == "salir":
            break
        print("\nAgente: ", end="")
        agent.run(user_input)
