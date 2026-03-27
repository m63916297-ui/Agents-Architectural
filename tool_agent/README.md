# Tool Agent

## Descripción

Agente de IA con **uso de herramientas externas** siguiendo el patrón **ReAct** (Reasoning + Acting). Puede buscar información, realizar cálculos y obtener información contextual mediante herramientas.

## Arquitectura

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        ARQUITECTURA TOOL AGENT                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│    ┌──────────────────────────────────────┐                            │
│    │           USER INPUT                    │                            │
│    │   "¿Qué hora es?" / "Busca X..."      │                            │
│    └──────────────────┬───────────────────┘                            │
│                        │                                                │
│                        ▼                                                │
│    ┌──────────────────────────────────────┐                            │
│    │         CICLO ReAct                    │                            │
│    │                                         │                            │
│    │   ┌────────────────────────────────┐  │                            │
│    │   │ 1. THOUGHT                     │  │                            │
│    │   │    "¿Qué necesito saber?"       │  │                            │
│    │   └────────────────┬───────────────┘  │                            │
│    │                    │                    │                            │
│    │                    ▼                    │                            │
│    │   ┌────────────────────────────────┐  │                            │
│    │   │ 2. ACTION                      │  │                            │
│    │   │    [Seleccionar Herramienta]    │  │                            │
│    │   │    • Buscar Wikipedia           │  │                            │
│    │   │    • Obtener Tiempo            │  │                            │
│    │   │    • Calculadora               │  │                            │
│    │   └────────────────┬───────────────┘  │                            │
│    │                    │                    │                            │
│    │                    ▼                    │                            │
│    │   ┌────────────────────────────────┐  │                            │
│    │   │ 3. OBSERVATION                │  │                            │
│    │   │    [Resultado de Herramienta]  │  │                            │
│    │   └────────────────┬───────────────┘  │                            │
│    │                    │                    │                            │
│    └────────────────────┼────────────────────┘                            │
│                         │                                                │
│                         ▼                                                │
│    ┌──────────────────────────────────────┐                            │
│    │         LLM (GPT-4)                   │                            │
│    │   Procesa observación y genera        │                            │
│    │   respuesta final                    │                            │
│    └──────────────────┬───────────────────┘                            │
│                       │                                                │
│                       ▼                                                │
│    ┌──────────────────────────────────────┐                            │
│    │         RESPONSE                      │                            │
│    └──────────────────────────────────────┘                            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## Cómo Funciona

1. **Entrada del Usuario**: Recibe una consulta o pregunta
2. **Razonamiento (Thought)**: Analiza qué tipo de información necesita
3. **Acción (Action)**: Selecciona y ejecuta la herramienta apropiada
4. **Observación (Observation)**: Recibe el resultado de la herramienta
5. **Respuesta (Response)**: Genera respuesta final con los datos obtenidos

## Herramientas Disponibles

| Herramienta | Función | Entrada |
|-------------|---------|---------|
| Tiempo Actual | Fecha y hora del sistema | Ninguna |
| Buscar Wikipedia | Búsqueda de información | Término de búsqueda |
| Calculadora | Operaciones matemáticas | Expresión |

## Características

- **Tipo:** Agente con Tool Use
- **Arquitectura:** ReAct (Reasoning + Acting)
- **Framework:** LangChain
- **Frontend:** Streamlit
- **Modelo:** GPT-4 / GPT-3.5-turbo

## Instalación

```bash
cd tool_agent
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
tool_agent/
├── agent.py           # Lógica con herramientas
├── app.py            # Interfaz Streamlit
├── requirements.txt  # Dependencias
├── .env.example     # Variables de entorno
└── README.md        # Este archivo
```

## Referencia

Basado en la arquitectura **Tool Use** documentada en `capability-papers/tool-use.md`:

> "ReAct: Synergizing Reasoning and Acting in Language Models" - Arxiv 2210.03629

> "HuggingGPT: Solving AI tasks with chat-gpt and its friends in huggingface" - Arxiv 2303.17580

> "OpenAGI: When LLM meets domain experts" - Arxiv 2304.04370
