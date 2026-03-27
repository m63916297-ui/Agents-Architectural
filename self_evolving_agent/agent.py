import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.memory import ConversationBufferMemory
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from typing import List, Dict

load_dotenv()


class SelfEvolvingAgent:
    """
    Self-Evolving Agent - Arquitectura con Auto-Evolución

    Este agente implementa capacidades de auto-mejora basadas en
    retroalimentación y aprendizaje de interacciones pasadas.

    Arquitectura:
    ┌─────────────────┐
    │  User Input      │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │   EXECUTE        │◄──── Ejecución normal
    │   (Ejecución)   │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │   EVALUATE       │◄──── Auto-evaluación
    │   (Evaluación)  │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │   LEARN          │◄──── Aprende de errores
    │   (Aprendizaje) │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │   UPDATE         │◄──── Mejora prompts/memory
    │   (Actualizar)  │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │   EVOLVED        │
    │   AGENT         │
    └─────────────────┘
    """

    def __init__(self, model_name: str = "gpt-4", temperature: float = 0.7):
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            streaming=True,
            callbacks=[StreamingStdOutCallbackHandler()],
        )

        self.memory = ConversationBufferMemory(
            memory_key="history", return_messages=True
        )

        self.learned_improvements = []
        self.interaction_count = 0

        self.system_prompt = """Eres un asistente de IA que aprende y evoluciona.
Después de cada interacción, evaluarás tu desempeño y te mejorarás."""

    def execute(self, user_input: str) -> str:
        """Ejecuta una interacción normal"""
        history = self.memory.load_memory_variables({}).get("history", [])

        messages = [
            SystemMessage(content=self.system_prompt),
            *history,
            HumanMessage(content=user_input),
        ]

        response = self.llm.invoke(messages)
        return response.content

    def evaluate_response(self, user_input: str, response: str) -> Dict:
        """Evalúa la calidad de su propia respuesta"""
        evaluation_prompt = f"""Evalúa la calidad de esta respuesta:

Pregunta: {user_input}
Respuesta: {response}

En una escala de 1-10, evalúa:
1. Relevancia
2. Precisión
3. Claridad
4. Utilidad

¿Hubo algún error o área de mejora?

Evalúa en formato JSON:"""

        messages = [
            SystemMessage(content="Eres un evaluador de respuestas."),
            HumanMessage(content=evaluation_prompt),
        ]

        evaluation = self.llm.invoke(messages).content

        return {
            "evaluation": evaluation,
            "needs_improvement": "áreas de mejora" in evaluation.lower()
            or "error" in evaluation.lower(),
        }

    def learn_from_feedback(self, user_input: str, response: str, feedback: str) -> str:
        """Aprende de la retroalimentación del usuario"""
        learning_prompt = f"""Analiza esta retroalimentación y genera una mejora:

Interacción:
- Pregunta: {user_input}
- Tu respuesta: {response}
- Retroalimentación: {feedback}

¿Qué aprendiste de esta retroalimentación?
¿Cómo mejorarás tu respuesta en el futuro?

Aprendizaje:"""

        messages = [
            SystemMessage(content="Eres un agente que aprende de sus errores."),
            HumanMessage(content=learning_prompt),
        ]

        learning = self.llm.invoke(messages).content
        self.learned_improvements.append(learning)

        improvement_note = f"""
        --- MEJORA APRENDIDA ---
        {learning}
        """

        self.system_prompt += improvement_note

        return learning

    def reflect_on_performance(self) -> str:
        """Reflexiona sobre su desempeño general"""
        reflection_prompt = f"""Reflexiona sobre tu desempeño en esta sesión:

Número de interacciones: {self.interaction_count}
Mejoras aprendidas: {len(self.learned_improvements)}

Últimas mejoras:
{chr(10).join(self.learned_improvements[-3:])}

¿Qué has mejorado?
¿En qué áreas sigues teniendo dificultades?
¿Qué consejos tienes para ti mismo?

Reflexión:"""

        messages = [
            SystemMessage(content="Eres un agente reflexivo."),
            HumanMessage(content=reflection_prompt),
        ]

        return self.llm.invoke(messages).content

    def run(self, user_input: str, user_feedback: str = None) -> Dict:
        """Ejecuta una interacción completa con auto-evolución"""
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

    def get_evolution_status(self) -> Dict:
        """Obtiene el estado de evolución del agente"""
        return {
            "interactions": self.interaction_count,
            "improvements_count": len(self.learned_improvements),
            "recent_improvements": self.learned_improvements[-3:],
            "system_prompt_length": len(self.system_prompt),
        }


if __name__ == "__main__":
    agent = SelfEvolvingAgent()
    print("Self-Evolving Agent - Agente con auto-evolución")
    print(
        "Comandos: 'feedback <texto>' = dar retroalimentación, 'status' = ver estado, 'salir' = terminar\n"
    )

    pending_feedback = None

    while True:
        user_input = input("\nTú: ")

        if user_input.lower() == "salir":
            break

        if user_input.lower().startswith("feedback "):
            pending_feedback = user_input[9:]
            print("Retroalimentación guardada para la próxima interacción.")
            continue

        if user_input.lower() == "status":
            status = agent.get_evolution_status()
            print(f"\n=== ESTADO DE EVOLUCIÓN ===")
            print(f"Interacciones: {status['interactions']}")
            print(f"Mejoras aprendidas: {status['improvements_count']}")
            continue

        print("\nAgente: ", end="")
        result = agent.run(user_input, pending_feedback)

        if pending_feedback:
            print(f"\n[Aprendizaje: {result['learning'][:100]}...]")
            pending_feedback = None

        if "reflection" in result:
            print(f"\n[Reflexión: {result['reflection'][:100]}...]")
