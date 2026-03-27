# Multi-Agent System

## Descripción

Sistema de **múltiples agentes especializados** que colaboran para resolver problemas complejos. Cada agente tiene un rol específico (investigador, analista, creador) y trabajan juntos bajo un orquestador.

## Arquitectura

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      ARQUITECTURA MULTI-AGENT                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│    ┌──────────────────────────────────────┐                            │
│    │           USER QUERY                     │                            │
│    │   "¿Cuáles son las tendencias IA?"      │                            │
│    └──────────────────┬───────────────────┘                            │
│                       │                                                │
│                       ▼                                                │
│    ┌──────────────────────────────────────┐                            │
│    │         ORCHESTRATOR (Maestro)         │                            │
│    │                                         │                            │
│    │   • Coordina la colaboración            │                            │
│    │   • Distribuye tareas                  │                            │
│    │   • Sintetiza resultados               │                            │
│    └──────────────────┬───────────────────┘                            │
│                       │                                                │
│         ┌─────────────┼─────────────┐                                │
│         │             │             │                                │
│         ▼             ▼             ▼                                │
│    ┌──────────┐ ┌──────────┐ ┌──────────┐                         │
│    │📚 INVEST │ │📊 ANALY │ │💡 CREATE │                         │
│    │          │ │          │ │          │                         │
│    │• Buscar  │ │• Analiz.│ │• Ideas   │                         │
│    │• Buscar  │ │• Compar. │ │• Creativ.│                         │
│    │• Citar   │ │• Evaluar │ │• Innovar │                         │
│    └────┬─────┘ └────┬─────┘ └────┬─────┘                         │
│         │             │             │                                │
│         └─────────────┼─────────────┘                                │
│                       │                                                │
│                       ▼                                                │
│    ┌──────────────────────────────────────┐                            │
│    │       COLLABORATIVE RESULTS             │                            │
│    │   Research + Analysis + Creativity      │                            │
│    └──────────────────┬───────────────────┘                            │
│                       │                                                │
│                       ▼                                                │
│    ┌──────────────────────────────────────┐                            │
│    │           SYNTHESIS                     │                            │
│    │   Respuesta final integrada             │                            │
│    └──────────────────────────────────────┘                            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## Agentes Especializados

| Agente | Rol | Funciones |
|--------|-----|-----------|
| 📚 Investigador | Búsqueda y análisis | Busca información, identifica fuentes, proporciona datos verificados |
| 📊 Analista | Evaluación crítica | Analiza patrones, compara alternativas, evalúa pros/contras |
| 💡 Creador | Generación de ideas | Propone soluciones innovadoras, explora posibilidades |

## Cómo Funciona

1. **Entrada del Usuario**: Recibe una consulta o problema
2. **Orquestación**: El orquestador coordina a los agentes
3. **Procesamiento Paralelo**: Cada agente procesa según su rol
4. **Colaboración**: Los resultados se combinan
5. **Síntesis**: Se genera una respuesta integrada final

## Características

- **Tipo:** Sistema Multi-Agente
- **Arquitectura:** Colaborativa con Orquestador
- **Framework:** LangChain
- **Frontend:** Streamlit
- **Modelo:** GPT-4 / GPT-3.5-turbo

## Instalación

```bash
cd multi_agent
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
multi_agent/
├── agent.py           # Sistema multi-agente
├── app.py            # Interfaz Streamlit
├── requirements.txt  # Dependencias
├── .env.example     # Variables de entorno
└── README.md        # Este archivo
```

## Referencia

Basado en la arquitectura **Multi-Agent** documentada en `agent-frameworks/agent-framework.md`:

> "CAMEL: Communicative Agents for Mind Exploration of Large Language Model Society" - Arxiv 2303.17760

> "MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework" - Arxiv 2308.00352

> "AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors" - Arxiv 2308.10848
