import streamlit as st

st.set_page_config(page_title="Market Research Generator", page_icon="📊")

st.title("📊 Market Research Generator")
st.markdown("Generate comprehensive market research reports")

if "product" not in st.session_state:
    st.session_state.product = ""
if "market" not in st.session_state:
    st.session_state.market = ""

col1, col2 = st.columns(2)
with col1:
    product = st.text_input(
        "Product/Service",
        value=st.session_state.product,
        placeholder="e.g., Electric Vehicles",
    )
with col2:
    market = st.text_input(
        "Target Market",
        value=st.session_state.market,
        placeholder="e.g., Global, US, Europe",
    )

market_type = st.selectbox("Market Focus", ["Consumer", "B2B", "B2C", "Industrial"])
time_horizon = st.selectbox(
    "Time Horizon",
    ["Short-term (1-2 years)", "Medium-term (3-5 years)", "Long-term (5-10 years)"],
)

if st.button("Generate Market Research", type="primary"):
    if product and market:
        st.session_state.product = product
        st.session_state.market = market

        with st.spinner("Analyzing market data..."):
            st.success("Market research generated successfully!")

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Market Size", "$45.2B")
            with col2:
                st.metric("CAGR", "12.5%")
            with col3:
                st.metric("Growth Rate", "+8.3%")
            with col4:
                st.metric("Market Share", "Yours: 2.1%")

            tabs = st.tabs(
                [
                    "Market Overview",
                    "Target Audience",
                    "Competitive Landscape",
                    "Opportunities",
                    "Recommendations",
                ]
            )

            with tabs[0]:
                st.markdown("## Market Overview")
                st.markdown(f"""
                The {product} market in {market} represents a significant opportunity with substantial growth potential.
                
                **Key Market Characteristics:**
                - Total Addressable Market (TAM): $45.2B
                - Serviceable Addressable Market (SAM): $12.8B
                - Serviceable Obtainable Market (SOM): $2.4B
                
                **Market Trends:**
                - Increasing consumer awareness
                - Regulatory support for innovation
                - Growing adoption rates
                - Technology advancements driving growth
                """)

            with tabs[1]:
                st.markdown("## Target Audience Analysis")

                st.markdown("### Primary Segments")
                segments = [
                    ("Early Adopters", "25-35", "Tech-savvy, high income", "30%"),
                    (
                        "Mainstream Users",
                        "35-50",
                        "Value-conscious, quality-focused",
                        "45%",
                    ),
                    ("Late Majority", "50-65", "Price-sensitive, traditional", "25%"),
                ]

                for name, age, characteristics, share in segments:
                    with st.expander(f"{name} ({share})"):
                        st.markdown(f"**Age Range:** {age}")
                        st.markdown(f"**Characteristics:** {characteristics}")

                st.markdown("### Buyer Personas:")
                st.markdown(
                    "1. **Tech Innovator**: Values cutting-edge features, willing to pay premium"
                )
                st.markdown(
                    "2. **Practical Professional**: Focuses on ROI and efficiency"
                )
                st.markdown(
                    "3. **Value Seeker**: Prioritizes cost-effectiveness and reliability"
                )

            with tabs[2]:
                st.markdown("## Competitive Landscape")

                st.markdown("### Major Players:")
                players = [
                    ("Company A", "25%", "Innovation leader"),
                    ("Company B", "20%", "Cost leader"),
                    ("Company C", "15%", "Niche specialist"),
                    ("Others", "40%", "Fragmented market"),
                ]

                for name, share, strategy in players:
                    st.markdown(f"- **{name}** ({share}): {strategy}")

                st.markdown("### Competitive Advantages:")
                st.markdown("- Technology differentiation")
                st.markdown("- Brand recognition")
                st.markdown("- Distribution network")
                st.markdown("- Customer loyalty programs")

            with tabs[3]:
                st.markdown("## Market Opportunities")

                opportunities = [
                    ("Emerging Markets", "High growth potential in developing regions"),
                    ("Product Innovation", "Untapped feature opportunities"),
                    ("Partnerships", "Strategic alliance possibilities"),
                    ("Digital Transformation", "Online channel expansion"),
                ]

                for title, desc in opportunities:
                    st.markdown(f"### {title}")
                    st.markdown(desc)
                    st.markdown("---")

            with tabs[4]:
                st.markdown("## Strategic Recommendations")

                recommendations = [
                    "Focus on differentiation through innovation",
                    "Target early adopters initially, then expand",
                    "Build strategic partnerships for market access",
                    "Invest in digital marketing and awareness",
                    "Develop tiered product offerings",
                    "Monitor competitive landscape closely",
                ]

                for i, rec in enumerate(recommendations, 1):
                    st.markdown(f"{i}. {rec}")

if st.button("Clear"):
    st.session_state.clear()
    st.rerun()
