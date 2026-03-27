# Planning Agent

## Descripción

Agente de IA especializado en **planificación y descomposición de tareas**. Transforma objetivos complejos en planes estructurados con sub-metas secuenciales y ejecutables.

## Arquitectura

```
┌─────────────────────────────────────────────────────────────────┐
│                    ARQUITECTURA PLANNING AGENT                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│    ┌──────────────────────────────────┐                         │
│    │          OBJETIVO PRINCIPAL       │                         │
│    │   "Crear una aplicación web..."    │                         │
│    └───────────────┬──────────────────┘                         │
│                    │                                             │
│                    ▼                                             │
│    ┌──────────────────────────────────┐                         │
│    │         PLANNER MODULE           │                         │
│    │                                   │                         │
│    │  ┌─────────────────────────────┐  │                         │
│    │  │  • Entender objetivo       │  │                         │
│    │  │  • Descomponer en sub-metas │  │                         │
│    │  │  • Establecer orden         │  │                         │
│    │  │  • Definir recursos         │  │                         │
│    │  └─────────────────────────────┘  │                         │
│    └───────────────┬──────────────────┘                         │
│                    │                                             │
│                    ▼                                             │
│    ┌──────────────────────────────────┐                         │
│    │         SUB-METAS CREADAS         │                         │
│    │                                   │                         │
│    │  1. Diseñar arquitectura         │                         │
│    │  2. Configurar entorno           │                         │
│    │  3. Implementar core features    │                         │
│    │  4. Testing                      │                         │
│    │  5. Deploy                       │                         │
│    └───────────────┬──────────────────┘                         │
│                    │                                             │
│                    ▼                                             │
│    ┌──────────────────────────────────┐                         │
│    │       EJECUTOR DE PLAN            │                         │
│    │   Completa cada sub-meta          │                         │
│    └──────────────────────────────────┘                         │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

## Cómo Funciona

1. **Entrada del Objetivo**: Recibe un objetivo complejo del usuario
2. **Análisis**: Comprende el objetivo y sus requerimientos
3. **Descomposición**: Divide en sub-metas manejables
4. **Ordenamiento**: Establece dependencias y secuencia lógica
5. **Plan**: Genera un plan estructurado
6. **Ejecución**: Completa cada paso del plan

## Características

- **Tipo:** Agente con capacidad de Planificación
- **Arquitectura:** Plan-and-Solve
- **Framework:** LangChain
- **Frontend:** Streamlit
- **Modelo:** GPT-4 / GPT-3.5-turbo

## Instalación

```bash
cd planning_agent
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
planning_agent/
├── agent.py           # Lógica de planificación
├── app.py            # Interfaz Streamlit
├── requirements.txt  # Dependencias
├── .env.example     # Variables de entorno
└── README.md        # Este archivo
```

## Métodos Disponibles

- `create_plan()`: Solo crea el plan sin ejecutar
- `execute_plan()`: Ejecuta un plan existente
- `plan_and_execute()`: Planifica y ejecuta en una sola llamada

## Referencia

Basado en la arquitectura **Planning** documentada en `capability-papers/planning.md`:

> "Plan-and-solve prompting: Improving zero-shot chain-of-thought reasoning" - Arxiv 2305.04091

> "Reasoning with Language Model is Planning with World Model" - Arxiv 2305.14992

> "LLM+P: Empowering Large Language Models with Optimal Planning Proficiency" - Arxiv 2304.11477
