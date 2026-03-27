import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage, SystemMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from typing import List, Dict

load_dotenv()


class PlanningAgent:
    """
    Planning Agent - Arquitectura con Planificación

    Este agente implementa capacidades de planificación de tareas,
    dividiendo objetivos complejos en sub-metas y pasos ejecutables.

    Arquitectura:
    ┌─────────────────┐
    │  Objetivo       │
    │  Principal      │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │   PLANNER       │◄──── Plan-and-Solve
    │   Module        │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │  Sub-metas      │
    │  (Descomposición)│
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │  Plan de        │
    │  Ejecución      │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │  Ejecución      │
    │  Secuencial     │
    └─────────────────┘
    """

    def __init__(self, model_name: str = "gpt-4", temperature: float = 0.3):
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            streaming=True,
            callbacks=[StreamingStdOutCallbackHandler()],
        )

        self.system_prompt = """Eres un asistente de IA especializado en planificación y descomposición de tareas.
Tu objetivo es transformar objetivos complejos en planes de acción estructurados.

Metodología:
1. ENTENDER: Comprende el objetivo final
2. DESCOMPONER: Divide en sub-metas manejables
3. ORDENAR: Establece dependencias y orden lógico
4. EJECUTAR: Completa cada paso secuencialmente
5. VERIFICAR: Confirma el cumplimiento del objetivo"""

        self.planning_template = PromptTemplate(
            input_variables=["goal"],
            template="""Objetivo: {goal}

Analiza este objetivo y crea un plan detallado:

## 1. ANÁLISIS DEL OBJETIVO
¿Qué exactamente se necesita lograr?

## 2. DESCOMPOSICIÓN EN SUB-METAS
Lista las sub-metas necesarias (usa formato numerado):
1. 
2. 
3.

## 3. ORDEN DE EJECUCIÓN
Especifica el orden y dependencias entre sub-metas:

## 4. PLAN DE ACCIÓN
Para cada sub-meta, indica:
- Qué hacer
- Recursos necesarios
- Tiempo estimado

## 5. VERIFICACIÓN
¿Cómo sabremos que el objetivo se cumplió?

Plan:""",
        )

    def create_plan(self, goal: str) -> Dict:
        """Crea un plan estructurado para alcanzar un objetivo"""
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=self.planning_template.format(goal=goal)),
        ]
        response = self.llm.invoke(messages)

        return {"goal": goal, "plan": response.content, "status": "planned"}

    def execute_plan(self, plan: str) -> str:
        """Ejecuta un plan previamente creado"""
        execution_prompt = f"""Ejecuta el siguiente plan paso a paso:

{plan}

Para cada paso completado, indícalo con ✓"""

        messages = [
            SystemMessage(
                content="Eres un executor de planes metódico. Ejecuta cada paso del plan."
            ),
            HumanMessage(content=execution_prompt),
        ]
        response = self.llm.invoke(messages)
        return response.content

    def plan_and_execute(self, goal: str) -> Dict:
        """Planifica y ejecuta un objetivo completo"""
        plan_result = self.create_plan(goal)
        execution_result = self.execute_plan(plan_result["plan"])

        return {
            "goal": goal,
            "plan": plan_result["plan"],
            "execution": execution_result,
            "status": "completed",
        }

    def run(self, goal: str) -> Dict:
        return self.plan_and_execute(goal)


if __name__ == "__main__":
    agent = PlanningAgent()
    print("Planning Agent - Descomposición y planificación de tareas")
    print("Escribe 'salir' para terminar\n")

    while True:
        goal = input("\nObjetivo: ")
        if goal.lower() == "salir":
            break
        result = agent.run(goal)
        print("\n=== RESULTADO ===")
        print(result)
