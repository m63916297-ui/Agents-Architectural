# Agentes de IA - Implementaciones con LangChain

Este directorio contiene implementaciones de diferentes arquitecturas de agentes de IA basadas en la documentación de `ai-agent-papers-main`. Cada agente implementa un patrón específico documentado en la literatura de investigación.

## Índice de Agentes

| Agente | Arquitectura | Descripción |
|--------|--------------|-------------|
| [simple_agent](simple_agent/) | Single-Agent | Agente básico con entrada/salida simple |
| [reasoning_agent](reasoning_agent/) | Chain-of-Thought | Razonamiento paso a paso |
| [planning_agent](planning_agent/) | Plan-and-Solve | Planificación y descomposición de tareas |
| [memory_agent](memory_agent/) | Conversation Memory | Memoria conversacional |
| [tool_agent](tool_agent/) | ReAct | Uso de herramientas externas |
| [multi_agent](multi_agent/) | Multi-Agent | Sistema de agentes colaborativos |
| [research_agent](research_agent/) | Agentic RAG | Búsqueda y síntesis de información |
| [deep_research_agent](deep_research_agent/) | Deep Research | Investigación profunda con verificación |
| [self_evolving_agent](self_evolving_agent/) | Self-Evolution | Auto-mejora continua |

## Estructura de cada Agente

```
agente/
├── agent.py           # Lógica principal del agente
├── app.py            # Interfaz Streamlit
├── requirements.txt  # Dependencias de Python
├── .env.example     # Variables de entorno ejemplo
└── README.md        # Documentación del agente
```

## Tecnologías

- **Framework:** LangChain
- **LLM:** OpenAI GPT-4 / GPT-3.5-turbo
- **Frontend:** Streamlit
- **Python:** 3.10+

## Instalación General

```bash
# Clonar y entrar al directorio
cd agentes-docs

# Instalar dependencias de un agente específico
cd <agente>
pip install -r requirements.txt

# Configurar API key
cp .env.example .env
# Editar .env y agregar OPENAI_API_KEY
```

## Uso Rápido

```bash
# Terminal
python agent.py

# Web (Streamlit)
streamlit run app.py
```

## Arquitectura General

```
┌─────────────────────────────────────────────────────────────────┐
│                    ARQUITECTURA DE AGENTES                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│    ┌──────────┐                                                │
│    │  User    │                                                │
│    │  Input   │                                                │
│    └────┬─────┘                                                │
│         │                                                       │
│         ▼                                                       │
│    ┌──────────────────────────────────────────┐                │
│    │         LANGCHAIN AGENT                      │                │
│    │                                             │                │
│    │  ┌────────────────────────────────────┐  │                │
│    │  │ Memory / Prompt / Tools           │  │                │
│    │  └────────────────────────────────────┘  │                │
│    │                  │                        │                │
│    │                  ▼                        │                │
│    │  ┌────────────────────────────────────┐  │                │
│    │  │      LLM (GPT-4 / GPT-3.5)        │  │                │
│    │  └────────────────────────────────────┘  │                │
│    └───────────────────┬──────────────────────┘                │
│                        │                                        │
│                        ▼                                        │
│    ┌──────────────────────────────────────────┐                │
│    │         Streamlit Frontend                 │                │
│    └──────────────────────────────────────────┘                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Mapeo con Documentación

### Agent Capabilities → Agentes

| Capability | Agente Implementado |
|------------|-------------------|
| Reasoning | reasoning_agent |
| Planning | planning_agent |
| Memory | memory_agent |
| Tool Use | tool_agent |
| Self-Evolution | self_evolving_agent |
| Evaluation | todos |

### Agent Frameworks → Agentes

| Framework | Agente Implementado |
|-----------|-------------------|
| Single-Agent | simple_agent |
| Multi-Agent | multi_agent |

### Applications → Agentes

| Application | Agente Implementado |
|-------------|-------------------|
| Research Agents | research_agent |
| Deep Research | deep_research_agent |
| Agentic AI Systems | multi_agent |

## Referencias

Basado en la documentación de `ai-agent-papers-main`:

- **Capability Papers:** Reasoning, Planning, Memory, Tool-use, Self-Evolution
- **Agent Frameworks:** Single-Agent, Multi-Agent
- **Application Papers:** Research Agents, Deep Research, Agentic Systems

## Licencia

MIT License
