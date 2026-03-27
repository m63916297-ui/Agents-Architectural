import streamlit as st

st.set_page_config(page_title="Literature Review Assistant", page_icon="📚")

st.title("📚 Literature Review Assistant")
st.markdown("Generate comprehensive literature reviews on any topic")

if "topic" not in st.session_state:
    st.session_state.topic = ""
if "research_depth" not in st.session_state:
    st.session_state.research_depth = 3
if "review" not in st.session_state:
    st.session_state.review = None

col1, col2 = st.columns([3, 1])
with col1:
    topic = st.text_input(
        "Research Topic",
        value=st.session_state.topic,
        placeholder="e.g., Climate Change Impact on Agriculture",
    )
with col2:
    depth = st.slider("Depth Level", 1, 5, st.session_state.research_depth)

if st.button("Generate Literature Review", type="primary"):
    if topic:
        with st.spinner("Conducting comprehensive literature review..."):
            sections = []

            sections.append("## Abstract")
            sections.append(
                f"This literature review examines the current state of research on **{topic}**. "
                f"The review synthesizes findings from multiple sources to provide a comprehensive overview."
            )

            sections.append("\n## Introduction")
            sections.append(f"### Background")
            sections.append(
                f"Research on {topic} has evolved significantly over the past decade. "
                f"This review aims to consolidate key findings and identify research gaps."
            )

            sections.append(f"\n### Research Questions")
            sections.append("1. What are the primary findings in this field?")
            sections.append("2. What methodological approaches are most common?")
            sections.append("3. What gaps exist in current research?")

            sections.append("\n## Main Findings")
            for i in range(min(depth, 5)):
                sections.append(f"\n### Theme {i + 1}: Key Area")
                sections.append(
                    f"Recent studies have revealed significant insights regarding {topic}. "
                    f"Research indicates multiple factors that contribute to understanding this complex topic."
                )

            sections.append("\n## Methodology Overview")
            sections.append("Common methodologies in this field include:")
            sections.append("- Quantitative analysis")
            sections.append("- Qualitative case studies")
            sections.append("- Mixed methods approaches")
            sections.append("- Systematic reviews")

            sections.append("\n## Research Gaps")
            sections.append("Despite extensive research, several gaps remain:")
            sections.append("1. Limited longitudinal studies")
            sections.append("2. Need for cross-cultural comparisons")
            sections.append("3. Integration of multiple theoretical frameworks")

            sections.append("\n## Conclusion")
            sections.append(
                f"This review highlights the complexity of {topic} and suggests "
                f"directions for future research to address identified gaps."
            )

            sections.append("\n## References")
            sections.append(
                "Note: In a production version, this would include actual citations from academic databases."
            )

            st.session_state.review = "\n".join(sections)
            st.session_state.topic = topic
            st.session_state.research_depth = depth

if st.session_state.review:
    st.divider()
    st.markdown(st.session_state.review)

    st.download_button(
        "📥 Download Review",
        st.session_state.review,
        file_name=f"literature_review_{st.session_state.topic.replace(' ', '_')}.md",
        mime="text/markdown",
    )

if st.button("Clear"):
    st.session_state.clear()
    st.rerun()
