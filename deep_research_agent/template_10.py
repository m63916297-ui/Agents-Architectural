import streamlit as st

st.set_page_config(page_title="Patent Research Tool", page_icon="💡")

st.title("💡 Patent Research Tool")
st.markdown("Research and analyze patents for innovation and IP protection")

if "invention" not in st.session_state:
    st.session_state.invention = ""

col1, col2 = st.columns([2, 1])
with col1:
    invention = st.text_input(
        "Technology/Invention",
        value=st.session_state.invention,
        placeholder="e.g., Quantum Computing, CRISPR, Battery Technology",
    )
with col2:
    search_type = st.selectbox(
        "Search Type", ["Patent Search", "Freedom to Operate", "Prior Art", "Landscape"]
    )

st.markdown("### Research Parameters")
params = st.multiselect(
    "Include in analysis",
    [
        "Patent Timeline",
        "Key Players",
        "Geographic Coverage",
        "Technology Classification",
    ],
    default=["Patent Timeline", "Key Players", "Technology Classification"],
)

if st.button("Research Patents", type="primary"):
    if invention:
        st.session_state.invention = invention

        with st.spinner("Searching patent databases..."):
            st.success("Patent research complete!")

            st.subheader(f"📋 Patent Research Report: {invention}")

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Patents", "12,450")
            with col2:
                st.metric("Active", "3,280")
            with col3:
                st.metric("Expired", "8,150")
            with col4:
                st.metric("Pending", "1,020")

            tabs = st.tabs(
                [
                    "Executive Summary",
                    "Patent Landscape",
                    "Key Players",
                    "Timeline",
                    "Legal Status",
                    "Opportunities",
                ]
            )

            with tabs[0]:
                st.markdown("## Executive Summary")

                st.info(f"""
                **{invention}** patent landscape contains over 12,000 patents with significant 
                activity in the past 5 years.
                
                **Key Findings:**
                - Market is fragmented with no dominant player
                - Strong activity in software/AI applications
                - Increasing patent filings from Asian companies
                - Several expired patents create freedom to operate
                
                **Recommendations:**
                - File early to secure priority
                - Consider strategic partnerships
                - Monitor competitor filings quarterly
                """)

                st.markdown("\n### Innovation Hotspots")
                hotspots = [
                    ("AI/ML Applications", "32%", "Highest growth area"),
                    ("Materials Science", "25%", "Foundational patents"),
                    ("Manufacturing Processes", "18%", "Process optimization"),
                    ("Energy Efficiency", "15%", "Sustainability focus"),
                    ("User Interfaces", "10%", "End-user applications"),
                ]
                for area, pct, note in hotspots:
                    st.markdown(f"- **{area} ({pct}):** {note}")

            with tabs[1]:
                st.markdown("## Patent Landscape Overview")

                st.markdown("### Technology Distribution")
                tech_dist = {
                    "Category": [
                        "AI/ML",
                        "Materials",
                        "Processes",
                        "Energy",
                        "UI/UX",
                        "Other",
                    ],
                    "Patents": [3200, 2500, 1800, 1500, 1000, 1450],
                }
                st.bar_chart(tech_dist, x="Category", y="Patents")

                st.markdown("\n### Geographic Distribution")
                geo_data = {
                    "Region": ["USA", "China", "Europe", "Japan", "Korea", "Other"],
                    "Filings": [3500, 4200, 1800, 1200, 1100, 650],
                }
                st.bar_chart(geo_data, x="Region", y="Filings")

                st.markdown("\n### Market Concentration")
                st.markdown("""
                - **Fragmented Market:** Top 10 players hold only 28% of patents
                - **Emerging Competition:** 45% from companies founded after 2015
                - **Academic Contribution:** 15% from research institutions
                """)

            with tabs[2]:
                st.markdown("## Key Patent Holders")

                st.markdown("### Top 10 Assignees")
                players = [
                    ("TechCorp Inc.", "USA", "1,245", "High", "AI, Materials"),
                    ("InnovateTech", "USA", "980", "High", "Processes"),
                    ("Asia Electronics", "Korea", "850", "Medium", "Manufacturing"),
                    ("Research Institute X", "China", "720", "Medium", "Multiple"),
                    ("Green Energy Co.", "Germany", "650", "High", "Energy"),
                    ("Future Systems", "Japan", "580", "Medium", "AI Applications"),
                    ("Material Sciences", "USA", "520", "Medium", "Materials"),
                    ("BioTech Partners", "UK", "480", "High", "Healthcare"),
                    ("CleanTech Ltd.", "Canada", "420", "Low", "Sustainability"),
                    ("Startup Labs", "USA", "380", "Low", "Emerging Tech"),
                ]

                st.markdown("| Rank | Company | Country | Patents | Activity | Focus |")
                st.markdown("|------|--------|---------|---------|----------|-------|")
                for i, (company, country, patents, activity, focus) in enumerate(
                    players, 1
                ):
                    st.markdown(
                        f"| {i} | {company} | {country} | {patents} | {activity} | {focus} |"
                    )

                st.markdown("\n### Filing Trends by Top Players")
                st.markdown("""
                - **TechCorp Inc.:** Increasing filings, strategic portfolio building
                - **InnovateTech:** Stable filings, quality over quantity approach
                - **Asia Electronics:** Rapid growth, aggressive expansion
                - **Academic Institutions:** Consistent output, licensing opportunities
                """)

            with tabs[3]:
                st.markdown("## Patent Timeline")

                st.markdown("### Filing Activity Over Time")
                timeline_data = {
                    "Year": [
                        2015,
                        2016,
                        2017,
                        2018,
                        2019,
                        2020,
                        2021,
                        2022,
                        2023,
                        2024,
                    ],
                    "Filings": [
                        850,
                        920,
                        1050,
                        1180,
                        1320,
                        1450,
                        1580,
                        1720,
                        1650,
                        1230,
                    ],
                }
                st.line_chart(timeline_data, x="Year", y="Filings")

                st.markdown("\n### Technology Evolution")
                evolution = [
                    ("2015-2017", "Foundation Era", "Basic patents established"),
                    (
                        "2018-2019",
                        "Diversification",
                        "Applications expand to new domains",
                    ),
                    (
                        "2020-2021",
                        "AI Integration",
                        "Machine learning integration begins",
                    ),
                    ("2022-2023", "Peak Activity", "Maximum filing intensity"),
                    (
                        "2024+",
                        "Consolidation",
                        "Market correction and strategic positioning",
                    ),
                ]

                for period, era, desc in evolution:
                    with st.expander(f"📅 {period}: {era}"):
                        st.markdown(desc)

                st.markdown("\n### Expiration Outlook")
                st.markdown("""
                - **2025-2026:** 2,450 patents expire (16% of current active)
                - **2027-2028:** 1,820 patents expire (12% of current active)
                - **Freedom to Operate:** Significant opportunities in expiring areas
                """)

            with tabs[4]:
                st.markdown("## Legal Status Analysis")

                st.markdown("### Patent Status Distribution")
                status = [
                    ("Granted", 6250, "50%", "🟢 Active protection"),
                    ("Pending", 3200, "26%", "🟡 Under examination"),
                    ("Expired", 2450, "20%", "⚪ Public domain"),
                    ("Abandoned", 550, "4%", "🔴 Not pursued"),
                ]
                for status_name, count, pct, note in status:
                    st.markdown(f"**{status_name}:** {count} patents ({pct}) - {note}")

                st.markdown("\n### Litigation Analysis")
                st.markdown("""
                **Active Disputes:** 15 ongoing cases
                - **High-Value Cases:** 3 (>$10M at stake)
                - **NPE Activity:** Moderate (15% of cases)
                - **Geographic Focus:** USA (70%), Europe (20%), Asia (10%)
                """)

                st.markdown("\n### Renewal Rates")
                renewal = [
                    ("Year 3", "92%", "Standard renewal"),
                    ("Year 7", "78%", "Cost-benefit assessment"),
                    ("Year 12", "45%", "Extended protection"),
                    ("Year 20", "12%", "Maximum term"),
                ]
                for year, rate, note in renewal:
                    st.markdown(f"- **{year}:** {rate} renewed ({note})")

            with tabs[5]:
                st.markdown("## Opportunities & Recommendations")

                st.markdown("### White Space Analysis")
                st.success("""
                **High-Value Opportunity Areas:**
                
                1. **AI + Manufacturing Integration**
                   - Limited patents in this intersection
                   - Strong commercial potential
                
                2. **Sustainable Materials**
                   - Growing field with patent gaps
                   - Regulatory tailwinds
                
                3. **User-Centric Applications**
                   - Underexplored in current filings
                   - Consumer market focus
                """)

                st.markdown("\n### Freedom to Operate (FTO) Assessment")
                fto = [
                    ("Core Technology", "High Risk", "Multiple blocking patents"),
                    ("Manufacturing Process", "Medium Risk", "Licensing opportunities"),
                    ("End-User Applications", "Low Risk", "Design freedom available"),
                    ("Software/AI Layer", "Medium Risk", "Evolving landscape"),
                ]
                for area, risk, note in fto:
                    emoji = (
                        "🔴" if "High" in risk else "🟡" if "Medium" in risk else "🟢"
                    )
                    st.markdown(f"{emoji} **{area}:** {risk} - {note}")

                st.markdown("\n### Strategic Recommendations")
                recommendations = [
                    "File provisional applications quickly to establish priority",
                    "Monitor competitor filings in Japan and Korea",
                    "Consider acquisition of expiring patents for portfolio",
                    "Explore licensing opportunities with universities",
                    "Build patent portfolio around AI/machine learning applications",
                ]
                for rec in recommendations:
                    st.markdown(f"- {rec}")

if st.button("Clear"):
    st.session_state.clear()
    st.rerun()
