import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()


class ReasoningAgent:
    """
    Reasoning Agent - Arquitectura con Chain-of-Thought

    Este agente implementa capacidades de razonamiento paso a paso,
    siguiendo el patron Chain-of-Thought (CoT).
    """

    def __init__(self, model_name: str = "gpt-4", temperature: float = 0.3):
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)

        self.system_prompt = """Eres un asistente de IA especializado en razonamiento paso a paso.
Tu objetivo es pensar de manera logica y sistemática antes de dar una respuesta.

Metodologia:
1. ANALIZAR: Entiende exactamente que se esta preguntando
2. RAZONAR: Divide el problema en pasos logicos
3. RESOLVER: Ejecuta cada paso mostrando tu razonamiento
4. CONCLUIR: Resume la respuesta final

Siempre muestra tu proceso de razonamiento antes de dar la respuesta final."""

        self.cot_template = PromptTemplate(
            input_variables=["question"],
            template="Pregunta: {question}\n\nRazonamiento paso a paso:\n",
        )

    def think(self, user_input: str) -> str:
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=self.cot_template.format(question=user_input)),
        ]
        response = self.llm.invoke(messages)
        return response.content

    def run(self, user_input: str) -> str:
        return self.think(user_input)

    def reason_about_problem(self, problem: str, domain: str = "general") -> dict:
        """Metodo especializado para razonamiento estructurado"""
        specialized_prompt = f"""Dominio: {domain}

Problema: {problem}

Estructura tu razonamiento:
1. COMPRENSION: Que es exactamente lo que se pide?
2. DATOS: Que informacion tengo disponible?
3. ESTRATEGIA: Que enfoque usare?
4. EJECUCION: Muestra los pasos de calculo/razonamiento
5. VERIFICACION: Es correcta mi respuesta?

Razonamiento:"""

        messages = [
            SystemMessage(
                content="Eres un experto en razonamiento estructurado. Responde siguiendo la estructura dada."
            ),
            HumanMessage(content=specialized_prompt),
        ]

        response = self.llm.invoke(messages)
        return {"problem": problem, "domain": domain, "reasoning": response.content}


if __name__ == "__main__":
    agent = ReasoningAgent()
    print("Reasoning Agent - Razonamiento paso a paso")
    print("Escribe 'salir' para terminar\n")

    while True:
        user_input = input("\nProblema: ")
        if user_input.lower() == "salir":
            break
        print("\nRazonamiento:")
        result = agent.run(user_input)
        print(result)
