import streamlit as st

st.set_page_config(page_title="Due Diligence Research", page_icon="⚖️")

st.title("⚖️ Due Diligence Research Tool")
st.markdown("Conduct comprehensive due diligence for investments and partnerships")

if "company_name" not in st.session_state:
    st.session_state.company_name = ""

col1, col2 = st.columns([2, 1])
with col1:
    company = st.text_input(
        "Company Name",
        value=st.session_state.company_name,
        placeholder="e.g., Acme Corporation",
    )
with col2:
    diligence_type = st.selectbox(
        "Type", ["Investment", "Acquisition", "Partnership", "M&A"]
    )

st.markdown("### Research Focus Areas")
focus_areas = st.multiselect(
    "Select areas to analyze",
    [
        "Financial Health",
        "Legal/Compliance",
        "Operational",
        "Market Position",
        "Technology",
        "Management",
        "Risks",
        "Opportunities",
    ],
    default=["Financial Health", "Market Position", "Risks"],
)

if st.button("Start Due Diligence", type="primary"):
    if company:
        st.session_state.company_name = company

        with st.spinner("Gathering due diligence data..."):
            st.success("Due diligence research complete!")

            st.subheader(f"📋 Due Diligence Report: {company}")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Overall Score", "78/100", "Good")
            with col2:
                st.metric("Risk Level", "Medium", "Low concern")
            with col3:
                st.metric("Recommendation", "Proceed", "With caution")

            tabs = st.tabs(["Overview"] + focus_areas[:3])

            with tabs[0]:
                st.markdown("## Executive Summary")
                st.info(f"""
                **{company}** is a {diligence_type} target with moderate risk profile 
                and acceptable return potential.
                
                **Key Highlights:**
                - Strong market position with 15% YoY growth
                - Stable financials with consistent profitability
                - Minimal legal/regulatory concerns
                - Experienced management team
                
                **Key Concerns:**
                - Increasing competition in core markets
                - Dependence on key customers (top 3 = 40% revenue)
                - Technology infrastructure needs upgrade
                
                **Recommendation:** Proceed with caution. Recommend further investigation 
                into customer concentration and technology roadmap.
                """)

                st.markdown("\n### Deal Parameters")
                deal_data = {
                    "Item": [
                        "Valuation",
                        "Revenue Multiple",
                        "EBITDA Multiple",
                        "Equity Stake",
                    ],
                    "Offered": ["$45M", "3.5x", "12x", "100%"],
                    "Sector Avg": ["$50M", "4.0x", "14x", "-"],
                }
                st.dataframe(deal_data, use_container_width=True)

            with tabs[1]:
                if "Financial Health" in focus_areas:
                    st.markdown("## Financial Health")

                    col_a, col_b = st.columns(2)
                    with col_a:
                        st.markdown("### Key Financial Metrics")
                        metrics = [
                            ("Revenue (LTM)", "$32.5M"),
                            ("Revenue Growth", "+18% YoY"),
                            ("Gross Margin", "62%"),
                            ("EBITDA", "$5.2M"),
                            ("Net Income", "$2.8M"),
                            ("Cash Position", "$8.5M"),
                        ]
                        for metric, value in metrics:
                            st.markdown(f"**{metric}:** {value}")

                    with col_b:
                        st.markdown("### Financial Health Score")
                        st.markdown("### 82/100")
                        st.progress(0.82, text="Strong financial position")

                        st.markdown("\n**Positives:**")
                        st.markdown("- Consistent profitability")
                        st.markdown("- Healthy cash flow")
                        st.markdown("- Low debt levels")

                        st.markdown("\n**Concerns:**")
                        st.markdown("- Revenue concentration")
                        st.markdown("- Margin pressure")

                    st.markdown("\n### 3-Year Financial Trend")
                    trend_data = {
                        "Year": ["2022", "2023", "2024"],
                        "Revenue": [25, 28, 32.5],
                        "EBITDA": [3.8, 4.5, 5.2],
                    }
                    st.line_chart(trend_data, x="Year", y=["Revenue", "EBITDA"])

            if "Legal/Compliance" in focus_areas and len(tabs) > 2:
                with tabs[2]:
                    st.markdown("## Legal & Compliance")

                    st.markdown("### Legal Status")
                    st.markdown("- **Entity Type:** Delaware C-Corp")
                    st.markdown("- **Incorporation:** 2018")
                    st.markdown("- **Good Standing:** ✅ Yes")

                    st.markdown("\n### Litigation Review")
                    st.markdown("**Active Lawsuits:** 1 (minor, IP dispute)")
                    st.markdown("**Historical:** 2 settled, no material impact")

                    st.markdown("\n### Compliance Status")
                    compliance = [
                        ("Data Privacy (GDPR/CCPA)", "Compliant", "✅"),
                        ("Industry Certifications", "Current", "✅"),
                        ("Environmental", "Compliant", "✅"),
                        ("Labor Law", "Compliant", "✅"),
                    ]

                    for item, status, icon in compliance:
                        st.markdown(f"{icon} **{item}:** {status}")

                    st.markdown("\n### Regulatory Risk: Low")
                    st.progress(0.2, text="Minimal regulatory exposure")

            if "Risks" in focus_areas and len(tabs) > 3:
                with tabs[3]:
                    st.markdown("## Risk Analysis")

                    risks = [
                        (
                            "Customer Concentration",
                            "High",
                            "Top 3 customers = 40% revenue",
                            "🔴",
                        ),
                        (
                            "Competitive Pressure",
                            "Medium",
                            "New entrants increasing",
                            "🟡",
                        ),
                        (
                            "Technology Obsolescence",
                            "Medium",
                            "Legacy systems need upgrade",
                            "🟡",
                        ),
                        (
                            "Key Person Dependence",
                            "Low",
                            "CEO critical to operations",
                            "🟢",
                        ),
                        ("Market Volatility", "Medium", "Sector-sensitive", "🟡"),
                        ("Regulatory Changes", "Low", "Minimal exposure", "🟢"),
                    ]

                    for risk, level, desc, icon in risks:
                        with st.expander(f"{icon} {risk} - {level}"):
                            st.markdown(f"**Description:** {desc}")
                            st.markdown(
                                f"**Mitigation:** Monitor and develop contingency plans"
                            )

                    st.markdown("\n### Overall Risk Score: Medium (45/100)")
                    st.progress(0.45, text="Acceptable risk profile")

if st.button("Clear"):
    st.session_state.clear()
    st.rerun()
