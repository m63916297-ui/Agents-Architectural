# Self-Evolving Agent

## Descripción

Agente de IA con **capacidades de auto-evolución**. Aprende de cada interacción, incorpora retroalimentación y mejora continuamente su comportamiento actualizando dinámicamente su prompt de sistema.

## Arquitectura

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ARQUITECTURA SELF-EVOLVING AGENT                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│    ┌──────────────────────────────────────┐                            │
│    │           USER INPUT                       │                            │
│    │   "Respuesta a mi pregunta..."           │                            │
│    └──────────────────┬───────────────────┘                            │
│                       │                                                │
│                       ▼                                                │
│    ┌──────────────────────────────────────┐                            │
│    │         EXECUTE PHASE                     │                            │
│    │                                         │                            │
│    │   1. Load memory                      │                            │
│    │   2. Build context (prompt + history)  │                            │
│    │   3. Invoke LLM                       │                            │
│    │   4. Return response                  │                            │
│    └──────────────────┬───────────────────┘                            │
│                       │                                                │
│                       ▼                                                │
│    ┌──────────────────────────────────────┐                            │
│    │         EVALUATE PHASE                    │                            │
│    │                                         │                            │
│    │   • Self-assessment (1-10 scale)       │                            │
│    │   • Identify errors                     │                            │
│    │   • Mark for improvement               │                            │
│    └──────────────────┬───────────────────┘                            │
│                       │                                                │
│                       ▼                                                │
│    ┌──────────────────────────────────────┐                            │
│    │         LEARN FROM FEEDBACK                │                            │
│    │                                         │                            │
│    │   Si hay retroalimentación:              │                            │
│    │   • Analyze feedback                     │                            │
│    │   • Extract improvement                  │                            │
│    │   • Add to learned_improvements         │                            │
│    └──────────────────┬───────────────────┘                            │
│                       │                                                │
│                       ▼                                                │
│    ┌──────────────────────────────────────┐                            │
│    │         UPDATE SYSTEM PROMPT               │                            │
│    │                                         │                            │
│    │   system_prompt += learned_improvement  │                            │
│    │                                         │                            │
│    │   El agente ahora tiene mayor           │                            │
│    │   conocimiento para futuras respuestas   │                            │
│    └──────────────────┬───────────────────┘                            │
│                       │                                                │
│                       ▼                                                │
│    ┌──────────────────────────────────────┐                            │
│    │         REFLECT PHASE (every 5)           │                            │
│    │                                         │                            │
│    │   • Analyze overall performance         │                            │
│    │   • Identify patterns                   │                            │
│    │   • Generate self-advice               │                            │
│    └──────────────────────────────────────┘                            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## Cómo Funciona

1. **Entrada del Usuario**: Recibe una pregunta o interacción
2. **Ejecución**: Procesa normalmente con memoria
3. **Evaluación**: Auto-evalúa su respuesta
4. **Retroalimentación**: Si hay feedback, aprende de él
5. **Actualización**: Mejora su system prompt con lo aprendido
6. **Reflexión**: Cada 5 interacciones, analiza su desempeño general

## Mecanismos de Evolución

| Mecanismo | Descripción |
|-----------|-------------|
| **Auto-Evaluación** | Califica su propia respuesta (1-10) |
| **Aprendizaje de Feedback** | Incorpora retroalimentación del usuario |
| **Actualización de Prompt** | Mejora dinámicamente el system prompt |
| **Reflexión Periódica** | Analiza patrones cada 5 interacciones |
| **Memoria Acumulativa** | Mantiene historial para contexto |

## Características

- **Tipo:** Agente Auto-Evolutivo
- **Arquitectura:** Self-Evolution
- **Framework:** LangChain
- **Frontend:** Streamlit
- **Modelo:** GPT-4 / GPT-3.5-turbo
- **Auto-mejora:** Sí (system prompt dinámico)

## Instalación

```bash
cd self_evolving_agent
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

## Comandos (Terminal)

- `feedback <texto>`: Dar retroalimentación
- `status`: Ver estado de evolución
- `salir`: Terminar sesión

## Estructura de Archivos

```
self_evolving_agent/
├── agent.py           # Lógica con auto-evolución
├── app.py            # Interfaz Streamlit
├── requirements.txt  # Dependencias
├── .env.example     # Variables de entorno
└── README.md        # Este archivo
```

## Estados del Agente

```python
{
    "interactions": 15,           # Contador de interacciones
    "improvements_count": 5,      # Mejoras aprendidas
    "recent_improvements": [...], # Últimas 3 mejoras
    "system_prompt_length": 2500  # Longitud del prompt
}
```

## Referencia

Basado en la arquitectura **Self-Evolution** documentada en `capability-papers/self-evolution.md`:

> "Self-Consolidation for Self-Evolving Agents" - Arxiv 2602.01966

> "Live-Evo: Online Evolution of Agentic Memory from Continuous Feedback" - Arxiv 2602.02369

> "MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents" - Arxiv 2602.02474
