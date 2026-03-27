import streamlit as st

st.set_page_config(page_title="Competitive Analysis Tool", page_icon="🔍")

st.title("🔍 Competitive Analysis Tool")
st.markdown("Analyze and compare competitors in any industry")

if "competitors" not in st.session_state:
    st.session_state.competitors = []
if "industry" not in st.session_state:
    st.session_state.industry = ""

col1, col2 = st.columns([2, 1])
with col1:
    industry = st.text_input(
        "Industry/Sector",
        value=st.session_state.industry,
        placeholder="e.g., SaaS, Fintech, E-commerce",
    )
with col2:
    num_competitors = st.number_input("Number of Competitors", 3, 10, 5)

if st.button("Generate Analysis", type="primary"):
    if industry:
        st.session_state.industry = industry

        competitors = [f"Competitor {i + 1}" for i in range(num_competitors)]
        st.session_state.competitors = competitors

        st.success("Analysis generated!")

        tabs = st.tabs(
            [
                "Overview",
                "Market Position",
                "Strengths & Weaknesses",
                "Comparison Table",
            ]
        )

        with tabs[0]:
            st.markdown("## Executive Summary")
            st.info(
                f"This competitive analysis examines {num_competitors} key players in the {industry} industry."
            )

            st.markdown("### Key Findings:")
            st.markdown(
                "- Market is moderately fragmented with several dominant players"
            )
            st.markdown(
                "- Technology differentiation is the primary competitive advantage"
            )
            st.markdown(
                "- Customer experience increasingly becoming a key differentiator"
            )

        with tabs[1]:
            st.markdown("## Market Position Map")
            st.markdown(
                "| Company | Market Share Est. | Price Range | Target Segment |"
            )
            st.markdown("|---------|------------------|-------------|----------------|")
            for comp in competitors[:5]:
                st.markdown(f"| {comp} | ~15-25% | $$ | Enterprise/SMB |")

            st.markdown("\n**Positioning Insights:**")
            st.markdown("- Premium segment: 2-3 established players")
            st.markdown("- Mid-market: Most competitive segment")
            st.markdown("- Budget: Emerging players gaining traction")

        with tabs[2]:
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown("### Strengths")
                for comp in competitors[:3]:
                    st.markdown(f"**{comp}:**")
                    st.markdown("- Strong brand recognition")
                    st.markdown("- Extensive distribution network")
                    st.markdown("- Robust technology platform")

            with col_b:
                st.markdown("### Weaknesses")
                for comp in competitors[:3]:
                    st.markdown(f"**{comp}:**")
                    st.markdown("- High price point")
                    st.markdown("- Limited customization")
                    st.markdown("- Slow innovation cycle")

        with tabs[3]:
            comparison_data = {
                "Feature": [
                    "Pricing",
                    "Features",
                    "Support",
                    "Integration",
                    "Scalability",
                ],
                "Competitor 1": ["$$$", "⭐⭐⭐⭐", "24/7", "50+", "Enterprise"],
                "Competitor 2": [
                    "$$",
                    "⭐⭐⭐",
                    "Business Hours",
                    "30+",
                    "SMB-Enterprise",
                ],
                "Competitor 3": ["$", "⭐⭐⭐⭐⭐", "Email Only", "20+", "SMB"],
            }
            st.dataframe(comparison_data, use_container_width=True)

if st.button("Clear"):
    st.session_state.clear()
    st.rerun()
