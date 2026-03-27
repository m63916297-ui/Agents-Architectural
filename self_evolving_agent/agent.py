import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.memory import ConversationBufferMemory
from typing import Optional

load_dotenv()


class SelfEvolvingAgent:
    """
    Self-Evolving Agent - Arquitectura con Auto-Evolucion

    Este agente implementa capacidades de auto-mejora basadas en
    retroalimentacion y aprendizaje de interacciones pasadas.
    """

    def __init__(self, model_name: str = "gpt-4", temperature: float = 0.7):
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)

        self.memory = ConversationBufferMemory(
            memory_key="history", return_messages=True
        )

        self.learned_improvements = []
        self.interaction_count = 0

        self.system_prompt = """Eres un asistente de IA que aprende y evoluciona.
Despues de cada interaccion, evaluaras tu desempeno y te mejoraras."""

    def execute(self, user_input: str) -> str:
        history = self.memory.load_memory_variables({}).get("history", [])

        messages = [
            SystemMessage(content=self.system_prompt),
            *history,
            HumanMessage(content=user_input),
        ]

        response = self.llm.invoke(messages)
        return response.content

    def evaluate_response(self, user_input: str, response: str) -> dict:
        evaluation_prompt = f"""Evalua la calidad de esta respuesta:

Pregunta: {user_input}
Respuesta: {response}

En una escala de 1-10, evalua:
1. Relevancia
2. Precision
3. Claridad
4. Utilidad

Evaluacion:"""

        messages = [
            SystemMessage(content="Eres un evaluador de respuestas."),
            HumanMessage(content=evaluation_prompt),
        ]

        evaluation = self.llm.invoke(messages).content

        return {
            "evaluation": evaluation,
            "needs_improvement": "area de mejora" in evaluation.lower()
            or "error" in evaluation.lower(),
        }

    def learn_from_feedback(self, user_input: str, response: str, feedback: str) -> str:
        learning_prompt = f"""Analiza esta retroalimentacion y genera una mejora:

Interaccion:
- Pregunta: {user_input}
- Tu respuesta: {response}
- Retroalimentacion: {feedback}

Aprendizaje:"""

        messages = [
            SystemMessage(content="Eres un agente que aprende de sus errores."),
            HumanMessage(content=learning_prompt),
        ]

        learning = self.llm.invoke(messages).content
        self.learned_improvements.append(learning)

        improvement_note = f"\n--- MEJORA APRENDIDA ---\n{learning}\n"
        self.system_prompt += improvement_note

        return learning

    def reflect_on_performance(self) -> str:
        reflection_prompt = f"""Reflexiona sobre tu desempeno en esta sesion:

Numero de interacciones: {self.interaction_count}
Mejoras aprendidas: {len(self.learned_improvements)}

Reflexion:"""

        messages = [
            SystemMessage(content="Eres un agente reflexivo."),
            HumanMessage(content=reflection_prompt),
        ]

        return self.llm.invoke(messages).content

    def run(self, user_input: str, user_feedback: Optional[str] = None) -> dict:
        response = self.execute(user_input)
        evaluation = self.evaluate_response(user_input, response)

        result = {
            "input": user_input,
            "response": response,
            "evaluation": evaluation,
            "learning": None,
        }

        if user_feedback:
            learning = self.learn_from_feedback(user_input, response, user_feedback)
            result["learning"] = learning

        self.memory.save_context({"user_input": user_input}, {"response": response})

        self.interaction_count += 1

        if self.interaction_count % 5 == 0:
            result["reflection"] = self.reflect_on_performance()

        return result

    def get_evolution_status(self) -> dict:
        return {
            "interactions": self.interaction_count,
            "improvements_count": len(self.learned_improvements),
            "recent_improvements": self.learned_improvements[-3:]
            if self.learned_improvements
            else [],
            "system_prompt_length": len(self.system_prompt),
        }


if __name__ == "__main__":
    agent = SelfEvolvingAgent()
    print("Self-Evolving Agent - Agente con auto-evolucion")
    print("Escribe 'salir' para terminar\n")

    pending_feedback = None

    while True:
        user_input = input("\nTu: ")

        if user_input.lower() == "salir":
            break

        if user_input.lower().startswith("feedback "):
            pending_feedback = user_input[9:]
            print("Retroalimentacion guardada.")
            continue

        if user_input.lower() == "status":
            status = agent.get_evolution_status()
            print(f"\n=== ESTADO DE EVOLUCION ===")
            print(f"Interacciones: {status['interactions']}")
            print(f"Mejoras aprendidas: {status['improvements_count']}")
            continue

        result = agent.run(user_input, pending_feedback)
        print(f"\nAgente: {result['response']}")

        if result.get("learning"):
            print(f"\n[Aprendizaje: {result['learning'][:100]}...]")

        if result.get("reflection"):
            print(f"\n[Reflexion: {result['reflection'][:100]}...]")
