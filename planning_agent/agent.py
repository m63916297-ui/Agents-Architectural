import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()


class PlanningAgent:
    """
    Planning Agent - Arquitectura con Planificacion

    Este agente implementa capacidades de planificacion de tareas,
    dividiendo objetivos complejos en sub-metas y pasos ejecutables.
    """

    def __init__(self, model_name: str = "gpt-4", temperature: float = 0.3):
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)

        self.system_prompt = """Eres un asistente de IA especializado en planificacion y descomposicion de tareas.
Tu objetivo es transformar objetivos complejos en planes de accion estructurados.

Metodologia:
1. ENTENDER: Comprende el objetivo final
2. DESCOMPONER: Divide en sub-metas manejables
3. ORDENAR: Establece dependencias y orden logico
4. EJECUTAR: Completa cada paso secuencialmente
5. VERIFICAR: Confirma el cumplimiento del objetivo"""

        self.planning_template = PromptTemplate(
            input_variables=["goal"],
            template="""Objetivo: {goal}

Analiza este objetivo y crea un plan detallado:

## 1. ANALISIS DEL OBJETIVO
Que exactamente se necesita lograr?

## 2. DESCOMPOSICION EN SUB-METAS
Lista las sub-metas necesarias (usa formato numerado):
1. 
2. 
3.

## 3. ORDEN DE EJECUCION
Especifica el orden y dependencias entre sub-metas:

## 4. PLAN DE ACCION
Para cada sub-meta, indica:
- Que hacer
- Recursos necesarios
- Tiempo estimado

## 5. VERIFICACION
Como sabremos que el objetivo se cumplio?

Plan:""",
        )

    def create_plan(self, goal: str) -> dict:
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

Para cada paso completado, indicarlo con marca de verificacion."""

        messages = [
            SystemMessage(
                content="Eres un executor de planes metodico. Ejecuta cada paso del plan."
            ),
            HumanMessage(content=execution_prompt),
        ]
        response = self.llm.invoke(messages)
        return response.content

    def plan_and_execute(self, goal: str) -> dict:
        """Planifica y ejecuta un objetivo completo"""
        plan_result = self.create_plan(goal)
        execution_result = self.execute_plan(plan_result["plan"])

        return {
            "goal": goal,
            "plan": plan_result["plan"],
            "execution": execution_result,
            "status": "completed",
        }

    def run(self, goal: str) -> dict:
        return self.plan_and_execute(goal)


if __name__ == "__main__":
    agent = PlanningAgent()
    print("Planning Agent - Descomposicion y planificacion de tareas")
    print("Escribe 'salir' para terminar\n")

    while True:
        goal = input("\nObjetivo: ")
        if goal.lower() == "salir":
            break
        result = agent.run(goal)
        print("\n=== RESULTADO ===")
        print(result)
