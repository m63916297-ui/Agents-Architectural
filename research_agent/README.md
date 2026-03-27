# Research Agent

## Descripción

Agente de IA especializado en **investigación automatizada**. Busca, extrae y sintetiza información de múltiples fuentes para generar reportes de investigación estructurados.

## Arquitectura

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      ARQUITECTURA RESEARCH AGENT                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│    ┌──────────────────────────────────────┐                            │
│    │           TOPIC / QUERY                   │                            │
│    │   "Impacto del cambio climático..."       │                            │
│    └──────────────────┬───────────────────┘                            │
│                       │                                                │
│                       ▼                                                │
│    ┌──────────────────────────────────────┐                            │
│    │         WEB SEARCH MODULE               │                            │
│    │                                         │                            │
│    │   • Wikipedia API                      │                            │
│    │   • News APIs                         │                            │
│    │   • Academic databases               │                            │
│    └──────────────────┬───────────────────┘                            │
│                       │                                                │
│                       ▼                                                │
│    ┌──────────────────────────────────────┐                            │
│    │         WEB SCRAPING                   │                            │
│    │                                         │                            │
│    │   • Extract relevant content          │                            │
│    │   • Clean and normalize              │                            │
│    │   • Store for processing             │                            │
│    └──────────────────┬───────────────────┘                            │
│                       │                                                │
│                       ▼                                                │
│    ┌──────────────────────────────────────┐                            │
│    │         INFORMATION PROCESSING           │                            │
│    │                                         │                            │
│    │   • Filter duplicates                │                            │
│    │   • Rank by relevance               │                            │
│    │   • Organize by themes              │                            │
│    └──────────────────┬───────────────────┘                            │
│                       │                                                │
│                       ▼                                                │
│    ┌──────────────────────────────────────┐                            │
│    │         LLM SYNTHESIS                  │                            │
│    │                                         │                            │
│    │   • Generate structured report        │                            │
│    │   • Cite sources                     │                            │
│    │   • Provide conclusions              │                            │
│    └──────────────────┬───────────────────┘                            │
│                       │                                                │
│                       ▼                                                │
│    ┌──────────────────────────────────────┐                            │
│    │         RESEARCH REPORT                  │                            │
│    │                                         │                            │
│    │   1. Resumen Ejecutivo               │                            │
│    │   2. Antecedentes                   │                            │
│    │   3. Hallazgos Principales          │                            │
│    │   4. Análisis                      │                            │
│    │   5. Conclusiones                  │                            │
│    └──────────────────────────────────────┘                            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## Cómo Funciona

1. **Entrada del Tema**: Recibe un tema de investigación
2. **Búsqueda Web**: Consulta múltiples fuentes (Wikipedia, news, etc.)
3. **Extracción**: Scraping de contenido relevante
4. **Procesamiento**: Filtra, organiza y rankea la información
5. **Síntesis LLM**: Genera un reporte estructurado
6. **Salida**: Reporte final con citas

## Características

- **Tipo:** Agente de Investigación
- **Arquitectura:** Agentic RAG
- **Framework:** LangChain
- **Frontend:** Streamlit
- **Modelo:** GPT-4 / GPT-3.5-turbo
- **Fuentes:** Wikipedia, News APIs

## Instalación

```bash
cd research_agent
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
research_agent/
├── agent.py           # Lógica de investigación
├── app.py            # Interfaz Streamlit
├── requirements.txt  # Dependencias
├── .env.example     # Variables de entorno
└── README.md        # Este archivo
```

## Reporte Generado

El agente produce reportes con esta estructura:
1. **Resumen Ejecutivo**
2. **Antecedentes**
3. **Hallazgos Principales**
4. **Análisis**
5. **Conclusiones**
6. **Fuentes**

## Referencia

Basado en la arquitectura **Research Agents** documentada en `application-papers/research-agents.md`:

> "OpenResearcher: Unleashing AI for Accelerated Scientific Research" - Arxiv 2408.06941

> "Agentic Information Retrieval" - Arxiv 2410.09713

> "MindSearch: Mimicking Human Minds Elicits Deep AI Searcher" - Arxiv 2407.20183
