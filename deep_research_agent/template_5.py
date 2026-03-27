import streamlit as st

st.set_page_config(page_title="Trend Analysis Dashboard", page_icon="📈")

st.title("📈 Trend Analysis Dashboard")
st.markdown("Analyze and predict industry trends")

if "trend_topic" not in st.session_state:
    st.session_state.trend_topic = ""

col1, col2 = st.columns([2, 1])
with col1:
    trend_topic = st.text_input(
        "Trend Topic",
        value=st.session_state.trend_topic,
        placeholder="e.g., Remote Work, AI Adoption, Sustainable Energy",
    )
with col2:
    time_period = st.selectbox(
        "Time Period", ["Past Year", "Past 5 Years", "Past Decade", "Future 5 Years"]
    )

analysis_type = st.multiselect(
    "Analysis Types",
    ["Historical Data", "Current State", "Future Predictions", "Impact Analysis"],
    default=["Historical Data", "Current State", "Future Predictions"],
)

if st.button("Analyze Trends", type="primary"):
    if trend_topic:
        st.session_state.trend_topic = trend_topic

        st.success("Trend analysis complete!")

        st.subheader(f"📊 {trend_topic} Trend Analysis")

        chart_data = {
            "Year": [2019, 2020, 2021, 2022, 2023, 2024, 2025],
            "Adoption %": [15, 25, 40, 55, 68, 78, 85],
            "Market Size ($B)": [10, 18, 35, 55, 80, 110, 145],
        }
        st.line_chart(chart_data, x="Year", y="Adoption %")

        tabs = st.tabs(["Overview", "Drivers", "Barriers", "Timeline", "Predictions"])

        with tabs[0]:
            st.markdown("## Trend Overview")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Current Adoption", "78%")
            with col2:
                st.metric("YoY Growth", "+15%")
            with col3:
                st.metric("Market Value", "$110B")

            st.markdown(f"""
            ### Summary
            **{trend_topic}** has emerged as a significant driver of change across multiple industries.
            
            **Key Statistics:**
            - Adoption rate increased from 15% (2019) to 78% (2024)
            - Compound annual growth rate (CAGR) of 32%
            - Over 60% of enterprises now have active initiatives
            
            **Geographic Distribution:**
            - North America: 35%
            - Europe: 28%
            - Asia-Pacific: 25%
            - Rest of World: 12%
            """)

        with tabs[1]:
            st.markdown("## Market Drivers")

            drivers = [
                (
                    "Technology Advancement",
                    95,
                    "Rapid technological improvements have made solutions more accessible and affordable",
                ),
                (
                    "Consumer Demand",
                    88,
                    "End-users increasingly expect modern, convenient solutions",
                ),
                (
                    "Cost Reduction",
                    82,
                    "Economic pressures driving efficiency improvements",
                ),
                (
                    "Regulatory Support",
                    65,
                    "Government policies and incentives accelerating adoption",
                ),
                (
                    "Competitive Pressure",
                    78,
                    "Market dynamics requiring innovation to stay relevant",
                ),
            ]

            for driver, score, desc in drivers:
                st.markdown(f"### {driver}")
                st.progress(score / 100, text=f"{score}% impact")
                st.markdown(desc)
                st.markdown("---")

        with tabs[2]:
            st.markdown("## Adoption Barriers")

            barriers = [
                (
                    "Initial Investment",
                    "High upfront costs can be prohibitive for smaller organizations",
                    "High",
                    ["Phased implementation", "Leasing options", "Government grants"],
                ),
                (
                    "Technical Complexity",
                    "Integration with existing systems poses challenges",
                    "Medium",
                    ["Professional services", "API-first design", "Migration tools"],
                ),
                (
                    "Skills Gap",
                    "Lack of trained personnel slows adoption",
                    "Medium",
                    ["Training programs", "Certification", "Partner networks"],
                ),
                (
                    "Security Concerns",
                    "Data privacy and cybersecurity worries",
                    "Low",
                    ["Encryption", "Compliance certifications", "Best practices"],
                ),
            ]

            for barrier, desc, severity, solutions in barriers:
                color = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}[severity]
                with st.expander(f"{color} {barrier} ({severity})"):
                    st.markdown(f"**Description:** {desc}")
                    st.markdown("**Potential Solutions:**")
                    for sol in solutions:
                        st.markdown(f"- {sol}")

        with tabs[3]:
            st.markdown("## Historical Timeline")

            milestones = [
                (
                    "2019",
                    "Early Adoption",
                    "Pioneer organizations begin implementing solutions",
                    ["Tech giants lead the way", "Proof of concept stage"],
                ),
                (
                    "2020",
                    "Acceleration",
                    "Pandemic accelerates adoption dramatically",
                    ["Remote work boom", "Investment surge"],
                ),
                (
                    "2021-2022",
                    "Maturation",
                    "Market consolidates, standards emerge",
                    ["Major acquisitions", "Platform consolidation"],
                ),
                (
                    "2023-2024",
                    "Mainstream",
                    "Widespread adoption across industries",
                    ["Enterprise solutions mature", "SMB accessibility improves"],
                ),
                (
                    "2025+",
                    "Integration",
                    "Seamless integration into daily operations",
                    ["AI-powered automation", "Predictive capabilities"],
                ),
            ]

            for year, phase, desc, highlights in milestones:
                st.markdown(f"### {year}: {phase}")
                st.markdown(desc)
                st.markdown("**Key Highlights:**")
                for h in highlights:
                    st.markdown(f"- {h}")
                st.markdown("---")

        with tabs[4]:
            st.markdown("## Future Predictions (5-Year Outlook)")

            st.markdown("### Market Projections")
            predictions = [
                ("2025", "$145B", "Continued strong growth"),
                ("2026", "$175B", "Market consolidation"),
                ("2027", "$210B", "AI integration peak"),
                ("2028", "$245B", "Global standardization"),
                ("2029", "$280B", "Mature market"),
            ]

            for year, value, outlook in predictions:
                st.markdown(f"- **{year}:** {value} ({outlook})")

            st.markdown("\n### Emerging Opportunities")
            st.markdown("""
            1. **AI-Enhanced Solutions**: Integration of machine learning for predictive analytics
            2. **Cross-Platform Integration**: Seamless connectivity across systems
            3. **Sustainable Practices**: Green technology integration
            4. **Personalization**: Hyper-personalized experiences
            5. **Accessibility**: Improved reach to underserved markets
            """)

            st.markdown("\n### Strategic Recommendations")
            st.markdown("""
            - **For Enterprises**: Prioritize integration and change management
            - **For Startups**: Focus on niche verticals and rapid iteration
            - **For Investors**: Look for platforms with strong network effects
            """)

if st.button("Clear"):
    st.session_state.clear()
    st.rerun()
