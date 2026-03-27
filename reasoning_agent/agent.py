import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage, SystemMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

load_dotenv()


class ReasoningAgent:
    """
    Reasoning Agent - Arquitectura con Chain-of-Thought

    Este agente implementa capacidades de razonamiento paso a paso,
    siguiendo el patrón Chain-of-Thought (CoT) documentado en la literatura.

    Arquitectura:
    ┌─────────────────┐
    │   User Input    │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │ Chain-of-Thought│◄──── Few-shot examples
    │ Prompt Template │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │   LLM (GPT-4)   │
    │  Step-by-Step   │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │  Reasoning Path  │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │   Final Answer  │
    └─────────────────┘
    """

    def __init__(self, model_name: str = "gpt-4", temperature: float = 0.3):
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            streaming=True,
            callbacks=[StreamingStdOutCallbackHandler()],
        )

        self.system_prompt = """Eres un asistente de IA especializado en razonamiento paso a paso.
Tu objetivo es pensar de manera lógica y sistemática antes de dar una respuesta.

Metodología:
1. ANALIZAR: Entiende exactamente qué se está preguntando
2. RAZONAR: Divide el problema en pasos lógicos
3. RESOLVER: Ejecuta cada paso mostrando tu razonamiento
4. CONCLUIR: Resume la respuesta final

Siempre muestra tu proceso de razonamiento antes de dar la respuesta final."""

        self.cot_template = PromptTemplate(
            input_variables=["question"],
            template="""Pregunta: {question}

Razonamiento paso a paso:
""",
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
        """Método especializado para razonamiento estructurado"""
        specialized_prompt = f"""Dominio: {domain}

Problema: {problem}

Estructura tu razonamiento:
1. COMPRENSIÓN: ¿Qué es exactamente lo que se pide?
2. DATOS: ¿Qué información tengo disponible?
3. ESTRATEGIA: ¿Qué enfoque usaré?
4. EJECUCIÓN: Muestra los pasos de cálculo/razonamiento
5. VERIFICACIÓN: ¿Es correcta mi respuesta?

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
