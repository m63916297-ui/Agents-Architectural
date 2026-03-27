# Memory Agent

## Descripción

Agente de IA con **gestión de memoria conversacional**. Mantiene contexto y coherencia a través de múltiples intercambios, recordando información previa de la conversación.

## Arquitectura

```
┌─────────────────────────────────────────────────────────────────┐
│                    ARQUITECTURA MEMORY AGENT                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                    │
│    ┌──────────────────────────────────┐                          │
│    │         USER INPUT                │                          │
│    │   "Recuerda lo que dijiste..."     │                          │
│    └───────────────┬──────────────────┘                          │
│                    │                                              │
│                    ▼                                              │
│    ┌──────────────────────────────────┐                          │
│    │       MEMORY BUFFER               │                          │
│    │                                    │                          │
│    │  ┌────────────────────────────┐  │                          │
│    │  │ Chat History (Últimos N)   │  │                          │
│    │  │ [user] + [assistant]       │  │                          │
│    │  │ [user] + [assistant]       │  │                          │
│    │  │ ...                        │  │                          │
│    │  └────────────────────────────┘  │                          │
│    └───────────────┬──────────────────┘                          │
│                    │                                              │
│                    ▼                                              │
│    ┌──────────────────────────────────┐                          │
│    │      CONTEXT + PROMPT             │                          │
│    │   System Prompt + History         │                          │
│    └───────────────┬──────────────────┘                          │
│                    │                                              │
│                    ▼                                              │
│    ┌──────────────────────────────────┐                          │
│    │         LLM (GPT-4)               │                          │
│    │   Con contexto de memoria         │                          │
│    └───────────────┬──────────────────┘                          │
│                    │                                              │
│                    ▼                                              │
│    ┌──────────────────────────────────┐                          │
│    │       SAVE TO MEMORY             │                          │
│    │   User + Response                │                          │
│    └──────────────────────────────────┘                          │
│                                                                    │
└─────────────────────────────────────────────────────────────────┘
```

## Cómo Funciona

1. **Entrada del Usuario**: Recibe un mensaje
2. **Carga de Memoria**: Obtiene historial conversacional
3. **Construcción de Prompt**: Combina system prompt + historial + input
4. **Procesamiento LLM**: Genera respuesta con contexto
5. **Guardado**: Almacena el intercambio en memoria
6. **Recorte**: Si la memoria es muy larga, elimina lo más antiguo

## Características

- **Tipo:** Agente con gestión de Memoria
- **Arquitectura:** ConversationBufferMemory
- **Framework:** LangChain
- **Frontend:** Streamlit
- **Modelo:** GPT-4 / GPT-3.5-turbo
- **Memoria:** Configurable (por defecto 10 intercambios)

## Instalación

```bash
cd memory_agent
pip install -r requirements.txt
cp .env.example .env
# Editar .env y agregar tu OPENAI_API_KEY
```

## Uso

```bash
# Terminal
python agent.py

# Web (Streamlit)
streamlit run app.py
```

## Estructura de Archivos

```
memory_agent/
├── agent.py           # Lógica con memoria
├── app.py            # Interfaz Streamlit
├── requirements.txt  # Dependencias
├── .env.example     # Variables de entorno
└── README.md        # Este archivo
```

## Comandos Especiales

- `memoria`: Ver historial de conversación
- `limpiar`: Borrar toda la memoria
- `salir`: Terminar sesión

## Referencia

Basado en la arquitectura **Memory** documentada en `capability-papers/memory.md`:

> "MemGPT: Towards LLMs as Operating Systems" - Arxiv 2310.08560

> "Memorybank: Enhancing large language models with long-term memory" - Arxiv 2305.10250

> "A Survey on the Memory Mechanism of Large Language Model based Agents" - Arxiv 2404.13501
