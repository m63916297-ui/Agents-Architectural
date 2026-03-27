# Reasoning Agent

## Descripción

Agente de IA especializado en **razonamiento paso a paso** utilizando la técnica Chain-of-Thought (CoT). Este agente descompone problemas complejos en pasos lógicos antes de generar una respuesta final.

## Arquitectura

```
┌─────────────────────────────────────────────────────────────────┐
│                   ARQUITECTURA REASONING AGENT                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│    ┌──────────┐                                                │
│    │  User    │                                                │
│    │  Input   │                                                │
│    └────┬─────┘                                                │
│         │                                                       │
│         ▼                                                       │
│    ┌────────────────────────────────────────┐                   │
│    │       CHAIN-OF-THOUGHT PROMPT          │                   │
│    │  "Razona paso a paso antes de         │                   │
│    │   responder..."                        │                   │
│    └────────────┬─────────────────────────┘                   │
│                 │                                               │
│                 ▼                                               │
│    ┌────────────────────────────────────────┐                   │
│    │              LLM (GPT-4)               │                   │
│    │                                         │                   │
│    │  Step 1: ANALIZAR problema             │                   │
│    │  Step 2: RAZONAR cada paso            │                   │
│    │  Step 3: RESOLVER cálculos            │                   │
│    │  Step 4: CONCLUIR respuesta           │                   │
│    └────────────┬─────────────────────────┘                   │
│                 │                                               │
│                 ▼                                               │
│    ┌────────────────────────────────────────┐                   │
│    │  Reasoning Path + Final Answer        │                   │
│    └────────────────────────────────────────┘                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Cómo Funciona

1. **Entrada del Usuario**: Recibe un problema o pregunta
2. **Prompt CoT**: Aplica el template de Chain-of-Thought
3. **Razonamiento Secuencial**: Genera pasos de razonamiento
4. **Respuesta Final**: Combina razonamiento + conclusión

## Características

- **Tipo:** Agente con capacidad de Razonamiento
- **Arquitectura:** Chain-of-Thought Prompting
- **Framework:** LangChain
- **Frontend:** Streamlit
- **Modelo:** GPT-4 / GPT-3.5-turbo

## Instalación

```bash
cd reasoning_agent
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
reasoning_agent/
├── agent.py           # Lógica con Chain-of-Thought
├── app.py            # Interfaz Streamlit
├── requirements.txt  # Dependencias
├── .env.example     # Variables de entorno
└── README.md        # Este archivo
```

## Métodos Disponibles

- `think()`: Razonamiento básico paso a paso
- `run()`: Alias para think()
- `reason_about_problem()`: Razonamiento estructurado por dominio

## Referencia

Basado en la arquitectura **Reasoning** documentada en `capability-papers/reasoning.md`:

> "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" - Arxiv 2201.11903

> "Self-consistency improves chain of thought reasoning in language models" - Arxiv 2203.11171

> "Tree of thoughts: Deliberate problem solving with large language models" - Arxiv 2305.10601
