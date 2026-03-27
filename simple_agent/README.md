# Simple Agent

## Descripción

Agente de IA básico que implementa la arquitectura **Single-Agent** (Agente Único). Este es el nivel más fundamental de agente, donde un solo modelo de lenguaje procesa entradas y genera salidas.

## Arquitectura

```
┌─────────────────────────────────────────────────────────────┐
│                    ARQUITECTURA SIMPLE AGENT               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│    ┌──────────┐                                             │
│    │  User    │                                             │
│    │  Input   │                                             │
│    └────┬─────┘                                             │
│         │                                                   │
│         ▼                                                   │
│    ┌──────────┐     ┌─────────────────┐                    │
│    │  Human   │────►│   System Prompt │                    │
│    │  Message │     │   (Predefinido) │                    │
│    └────┬─────┘     └────────┬────────┘                    │
│         │                    │                              │
│         │    ┌───────────────┘                              │
│         │    │                                              │
│         ▼    ▼                                              │
│    ┌────────────────────────────────┐                       │
│    │         LLM (GPT-4)            │                       │
│    │   - Reasoning                  │                       │
│    │   - Response Generation       │                       │
│    └───────────────┬────────────────┘                       │
│                    │                                        │
│                    ▼                                        │
│    ┌────────────────────────────────┐                       │
│    │         Response               │                       │
│    └────────────────────────────────┘                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Cómo Funciona

1. **Entrada del Usuario**: El usuario envía un mensaje de texto
2. **Construcción del Prompt**: Se combina el mensaje del usuario con un prompt de sistema predefinido
3. **Procesamiento LLM**: El modelo de lenguaje procesa el prompt y genera una respuesta
4. **Salida**: La respuesta se muestra al usuario

## Características

- **Tipo:** Single-Agent (Agente Único)
- **Framework:** LangChain
- **Frontend:** Streamlit
- **Modelo:** GPT-4 / GPT-3.5-turbo (configurable)
- **Temperatura:** Ajustable (0.0 - 1.0)

## Instalación

```bash
cd simple_agent
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
simple_agent/
├── agent.py           # Lógica principal del agente
├── app.py            # Interfaz Streamlit
├── requirements.txt  # Dependencias
├── .env.example     # Variables de entorno ejemplo
└── README.md        # Este archivo
```

## Referencia

Basado en la arquitectura **Single-Agent** documentada en `agent-frameworks/agent-framework.md`:

> "Agents: An Open-source Framework for Autonomous Language Agents" - Arxiv 2309.07870
