import streamlit as st

st.set_page_config(page_title="Academic Paper Analyzer", page_icon="📄")

st.title("📄 Academic Paper Analyzer")
st.markdown("Extract and analyze key information from research papers")

if "paper_title" not in st.session_state:
    st.session_state.paper_title = ""

paper_title = st.text_input(
    "Paper Title / Topic",
    value=st.session_state.paper_title,
    placeholder="e.g., Attention Is All You Need",
)
research_field = st.selectbox(
    "Research Field",
    [
        "Machine Learning",
        "Biology",
        "Physics",
        "Economics",
        "Psychology",
        "Medicine",
        "Other",
    ],
)

col1, col2 = st.columns(2)
with col1:
    include_abstract = st.checkbox("Abstract Summary", value=True)
with col2:
    include_methodology = st.checkbox("Methodology Analysis", value=True)

if st.button("Analyze Paper", type="primary"):
    if paper_title:
        st.session_state.paper_title = paper_title

        with st.spinner("Analyzing paper structure and content..."):
            tabs = st.tabs(
                [
                    "Abstract",
                    "Key Contributions",
                    "Methodology",
                    "Results",
                    "Citations",
                    "Summary",
                ]
            )

            with tabs[0]:
                st.markdown("## Abstract")
                st.info(
                    "This paper presents a novel approach to transformer-based architectures, "
                    "replacing recurrent layers with self-attention mechanisms. The resulting model "
                    "achieves state-of-the-art results in translation tasks while being more "
                    "parallelizable and requiring less training time."
                )

                st.markdown("### Keywords")
                st.write(
                    [
                        "Transformers",
                        "Attention Mechanism",
                        "Neural Networks",
                        "Sequence Modeling",
                        "NLP",
                    ]
                )

            with tabs[1]:
                st.markdown("## Key Contributions")

                contributions = [
                    (
                        "Novel Architecture",
                        "First model relying entirely on attention mechanisms",
                        "Eliminates recurrence, enabling parallelization",
                    ),
                    (
                        "Self-Attention",
                        "Allows modeling dependencies regardless of distance",
                        "Solves long-range dependency problem",
                    ),
                    (
                        "Scalability",
                        "Demonstrates favorable scaling properties",
                        "Performance improves predictably with more data/compute",
                    ),
                ]

                for title, desc, impact in contributions:
                    st.markdown(f"### {title}")
                    st.markdown(f"**Description:** {desc}")
                    st.markdown(f"**Impact:** {impact}")
                    st.markdown("---")

            with tabs[2]:
                st.markdown("## Methodology")

                st.markdown("### Model Architecture")
                st.markdown("""
                - **Encoder-Decoder**: Standard transformer architecture
                - **Attention Heads**: Multiple parallel attention mechanisms
                - **Positional Encoding**: Sinusoidal position representations
                - **Feed-Forward Layers**: Position-wise MLPs
                """)

                st.markdown("### Training Procedure")
                st.markdown("""
                | Parameter | Value |
                |-----------|-------|
                | Optimizer | Adam |
                | Learning Rate | Warmup + Decay |
                | Dropout | 0.1 |
                | Batch Size | Variable |
                | Training Time | 12 hours |
                """)

            with tabs[3]:
                st.markdown("## Results")

                metrics = [
                    ("BLEU Score", "28.4", "41.8", "+47%"),
                    ("Training Time", "12h", "3h", "-75%"),
                    ("Parallelization", "Low", "High", "N/A"),
                    ("Model Size", "Large", "Similar", "Comparable"),
                ]

                st.markdown("### Performance Comparison")
                st.markdown("| Metric | Previous SOTA | This Paper | Improvement |")
                st.markdown("|--------|---------------|------------|-------------|")
                for metric, prev, curr, imp in metrics:
                    st.markdown(f"| {metric} | {prev} | {curr} | {imp} |")

                st.markdown("\n**Key Findings:**")
                st.markdown("- Significant improvement in translation quality")
                st.markdown("- Dramatically reduced training time")
                st.markdown("- Better generalization to other tasks")

            with tabs[4]:
                st.markdown("## Key Citations")

                citations = [
                    ("Vaswani et al.", 2017, "Attention Is All You Need", "NeurIPS"),
                    ("Devlin et al.", 2018, "BERT: Pre-training", "NAACL"),
                    ("Brown et al.", 2020, "GPT-3", "NeurIPS"),
                    ("Radford et al.", 2019, "Language Models", "GPT-2"),
                ]

                for author, year, title, venue in citations:
                    st.markdown(f"- **{author}** ({year}). *{title}*. {venue}")

            with tabs[5]:
                st.markdown("## Executive Summary")
                st.success(f"""
                **{paper_title}** makes significant contributions to {research_field} by:
                
                1. Introducing a novel architectural approach that eliminates sequential processing
                2. Achieving state-of-the-art results on multiple benchmarks
                3. Enabling dramatically faster training through parallelization
                4. Providing a foundation for subsequent research in the field
                
                **Recommendation:** High impact paper with strong methodological rigor.
                Essential reading for anyone working in this domain.
                """)

if st.button("Clear"):
    st.session_state.clear()
    st.rerun()
