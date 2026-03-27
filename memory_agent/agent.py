import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.memory import ConversationBufferMemory

load_dotenv()


class MemoryAgent:
    """
    Memory Agent - Arquitectura con Gestion de Memoria

    Este agente implementa gestion de memoria conversacional,
    permitiendo mantener contexto a traves de multiples interacciones.
    """

    def __init__(
        self,
        model_name: str = "gpt-4",
        temperature: float = 0.7,
        memory_limit: int = 10,
    ):
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)

        self.memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True, output_key="response"
        )

        self.memory_limit = memory_limit

        self.system_prompt = f"""Eres un asistente de IA con memoria conversacional.
Puedes recordar contexto de conversaciones anteriores en esta sesion.

Caracteristicas:
- Recuerdas el contexto previo de la conversacion
- Mantienes coherencia en conversaciones largas
- Puedes referenciar informacion mencionada anteriormente
- Olvidas informacion muy antigua (mas de {memory_limit} intercambios) para mantener eficiencia"""

    def chat(self, user_input: str) -> str:
        messages = [SystemMessage(content=self.system_prompt)]

        history = self.memory.load_memory_variables({}).get("chat_history", [])
        messages.extend(history)
        messages.append(HumanMessage(content=user_input))

        response = self.llm.invoke(messages)

        self.memory.save_context(
            {"user_input": user_input}, {"response": response.content}
        )

        self._trim_memory()

        return response.content

    def _trim_memory(self):
        """Mantiene la memoria dentro del limite permitido"""
        history = self.memory.chat_memory.messages
        if len(history) > self.memory_limit * 2:
            self.memory.chat_memory.messages = history[-self.memory_limit * 2 :]

    def get_memory(self) -> list:
        """Obtiene el historial de conversacion"""
        history = self.memory.load_memory_variables({}).get("chat_history", [])
        return [
            {"role": "user" if i % 2 == 0 else "assistant", "content": msg.content}
            for i, msg in enumerate(history)
        ]

    def clear_memory(self):
        """Limpia el historial de conversacion"""
        self.memory.clear()
        return "Memoria limpiada exitosamente"

    def run(self, user_input: str) -> str:
        return self.chat(user_input)


if __name__ == "__main__":
    agent = MemoryAgent()
    print("Memory Agent - Conversacion con memoria")
    print(
        "Comandos: 'memoria' = ver historial, 'limpiar' = borrar memoria, 'salir' = terminar\n"
    )

    while True:
        user_input = input("\nTu: ")
        if user_input.lower() == "salir":
            break
        elif user_input.lower() == "memoria":
            history = agent.get_memory()
            print("\n=== HISTORIAL ===")
            for msg in history:
                print(f"[{msg['role']}]: {msg['content'][:100]}...")
        elif user_input.lower() == "limpiar":
            print(agent.clear_memory())
        else:
            print("\nAgente:", agent.run(user_input))
