# Deep Research Agent

## Descripción

Agente de IA especializado en **investigación profunda automatizada**. Combina búsqueda iterativa, verificación de información y síntesis para generar reportes comprehensivos con estándares académicos.

## Arquitectura

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ARQUITECTURA DEEP RESEARCH AGENT                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│    ┌──────────────────────────────────────┐                            │
│    │           USER QUERY                       │                            │
│    │   "Impacto de la IA en el mercado..."     │                            │
│    └──────────────────┬───────────────────┘                            │
│                       │                                                │
│                       ▼                                                │
│    ┌──────────────────────────────────────┐                            │
│    │         QUERY PLANNER                     │                            │
│    │                                         │                            │
│    │   Descompone la consulta en:           │                            │
│    │   • Subtema 1                          │                            │
│    │   • Subtema 2                          │                            │
│    │   • Subtema 3                          │                            │
│    │   • Subtema N...                       │                            │
│    └──────────────────┬───────────────────┘                            │
│                       │                                                │
│         ┌─────────────┼─────────────┐                                │
│         │             │             │                                │
│         ▼             ▼             ▼                                │
│    ┌──────────────────────────────────────┐                            │
│    │         ITERATIVE RESEARCH                │                            │
│    │                                         │                            │
│    │   Para cada subtema:                    │                            │
│    │   ┌────────────────────────────────┐  │                            │
│    │   │ 1. Wikipedia Search            │  │                            │
│    │   │ 2. News Search                 │  │                            │
│    │   │ 3. Academic Search              │  │                            │
│    │   │ 4. Cross-reference             │  │                            │
│    │   └────────────────────────────────┘  │                            │
│    └──────────────────┬───────────────────┘                            │
│                       │                                                │
│                       ▼                                                │
│    ┌──────────────────────────────────────┐                            │
│    │         VERIFICATION LAYER                │                            │
│    │                                         │                            │
│    │   • Check consistency                 │                            │
│    │   • Validate sources                 │                            │
│    │   • Identify gaps                    │                            │
│    └──────────────────┬───────────────────┘                            │
│                       │                                                │
│                       ▼                                                │
│    ┌──────────────────────────────────────┐                            │
│    │         DEEP SYNTHESIS                    │                            │
│    │                                         │                            │
│    │   LLM genera reporte comprehensivo:     │                            │
│    │   • Executive Summary                  │                            │
│    │   • Detailed Analysis                  │                            │
│    │   • Critical Discussion                │                            │
│    │   • Conclusions & Recommendations     │                            │
│    └──────────────────┬───────────────────┘                            │
│                       │                                                │
│                       ▼                                                │
│    ┌──────────────────────────────────────┐                            │
│    │         DEEP RESEARCH REPORT               │                            │
│    │                                         │                            │
│    │   Formato académico completo:           │                            │
│    │   1. Resumen Ejecutivo                │                            │
│    │   2. Introducción                     │                            │
│    │   3. Análisis Detallado              │                            │
│    │   4. Hallazgos                       │                            │
│    │   5. Discusión                        │                            │
│    │   6. Conclusiones                    │                            │
│    │   7. Recomendaciones                  │                            │
│    └──────────────────────────────────────┘                            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## Cómo Funciona

1. **Entrada de Consulta**: Recibe una consulta de investigación
2. **Planificación**: Descompone en subtemas específicos
3. **Investigación Iterativa**: Para cada subtema:
   - Busca en Wikipedia
   - Busca en noticias
   - Cruza referencias
4. **Verificación**: Valida consistencia y fuentes
5. **Síntesis Profunda**: Genera reporte completo con estándares académicos

## Características

- **Tipo:** Agente de Investigación Profunda
- **Arquitectura:** Deep Research con Verificación
- **Framework:** LangChain
- **Frontend:** Streamlit
- **Modelo:** GPT-4 / GPT-3.5-turbo
- **Metodología:** Iterativa con auto-verificación

## Instalación

```bash
cd deep_research_agent
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
deep_research_agent/
├── agent.py           # Lógica de investigación profunda
├── app.py            # Interfaz Streamlit
├── requirements.txt  # Dependencias
├── .env.example     # Variables de entorno
└── README.md        # Este archivo
```

## Estructura del Reporte

El agente genera reportes con esta estructura:
1. **Resumen Ejecutivo** (200 palabras)
2. **Introducción y Contexto**
3. **Análisis Detallado** (por subtemas)
4. **Hallazgos Principales**
5. **Discusión y Análisis Crítico**
6. **Limitaciones**
7. **Conclusiones**
8. **Recomendaciones**
9. **Fuentes y Citas**

## Referencia

Basado en la arquitectura **Deep Research Agents** documentada en `application-papers/deep-research-agents.md`:

> "Deep Research: A Systematic Survey" - Arxiv 2512.02038

> "How Far Are We from Genuinely Useful Deep Research Agents?" - Arxiv 2512.01948

> "Deep Research Agents: A Systematic Examination And Roadmap" - Arxiv 2506.18096
