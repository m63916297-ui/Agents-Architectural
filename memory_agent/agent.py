import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from typing import List, Dict

load_dotenv()


class MemoryAgent:
    """
    Memory Agent - Arquitectura con Gestión de Memoria

    Este agente implementa gestión de memoria conversacional,
    permitiendo mantener contexto a través de múltiples interacciones.

    Arquitectura:
    ┌─────────────────┐
    │  User Input     │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │    MEMORIA      │◄──── Conversation History
    │  (Buffer)       │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │   LLM (GPT-4)   │
    │  + Contexto      │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │  Respuesta       │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │  Guardar en     │
    │  Memoria         │
    └─────────────────┘
    """

    def __init__(
        self,
        model_name: str = "gpt-4",
        temperature: float = 0.7,
        memory_limit: int = 10,
    ):
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            streaming=True,
            callbacks=[StreamingStdOutCallbackHandler()],
        )

        self.memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True, output_key="response"
        )

        self.memory_limit = memory_limit

        self.system_prompt = """Eres un asistente de IA con memoria conversacional.
Puedes recordar contexto de conversaciones anteriores en esta sesión.

Características:
- Recuerdas el contexto previo de la conversación
- Mantienes coherencia en conversaciones largas
- Puedes referenciar información mencionada anteriormente
- Olvidas información muy antigua (>{} intercambios) para mantener eficiencia

""".format(memory_limit)

    def chat(self, user_input: str) -> str:
        messages = [
            SystemMessage(content=self.system_prompt),
            *self.memory.load_memory_variables({}).get("chat_history", []),
        ]

        chat_prompt = ChatPromptTemplate.from_messages(messages)
        prompt_with_history = chat_prompt.append(HumanMessage(content=user_input))

        response = self.llm.invoke(
            [SystemMessage(content=self.system_prompt)]
            + self.memory.load_memory_variables({}).get("chat_history", [])
            + [HumanMessage(content=user_input)]
        )

        self.memory.save_context(
            {"user_input": user_input}, {"response": response.content}
        )

        self._trim_memory()

        return response.content

    def _trim_memory(self):
        """Mantiene la memoria dentro del límite permitido"""
        history = self.memory.chat_memory.messages
        if len(history) > self.memory_limit * 2:
            self.memory.chat_memory.messages = history[-self.memory_limit * 2 :]

    def get_memory(self) -> List[Dict]:
        """Obtiene el historial de conversación"""
        history = self.memory.load_memory_variables({}).get("chat_history", [])
        return [
            {
                "role": "user" if isinstance(m, HumanMessage) else "assistant",
                "content": m.content,
            }
            for m in history
        ]

    def clear_memory(self):
        """Limpia el historial de conversación"""
        self.memory.clear()
        return "Memoria limpiada exitosamente"

    def run(self, user_input: str) -> str:
        return self.chat(user_input)


if __name__ == "__main__":
    agent = MemoryAgent()
    print("Memory Agent - Conversación con memoria")
    print(
        "Comandos: 'memoria' = ver historial, 'limpiar' = borrar memoria, 'salir' = terminar\n"
    )

    while True:
        user_input = input("\nTú: ")
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
            print("\nAgente: ", end="")
            agent.run(user_input)
