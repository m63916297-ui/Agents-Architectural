import streamlit as st

st.set_page_config(page_title="Consumer Behavior Analysis", page_icon="🛒")

st.title("🛒 Consumer Behavior Analysis")
st.markdown("Analyze consumer patterns and behavior for business insights")

if "product_category" not in st.session_state:
    st.session_state.product_category = ""

col1, col2 = st.columns([2, 1])
with col1:
    category = st.text_input(
        "Product Category",
        value=st.session_state.product_category,
        placeholder="e.g., Electronics, Fashion, Food & Beverage",
    )
with col2:
    region = st.selectbox(
        "Region", ["Global", "North America", "Europe", "Asia-Pacific", "Latin America"]
    )

demographics = st.multiselect(
    "Target Demographics",
    ["Gen Z (18-25)", "Millennials (26-41)", "Gen X (42-57)", "Boomers (58-76)"],
    default=["Millennials (26-41)", "Gen X (42-57)"],
)

if st.button("Analyze Behavior", type="primary"):
    if category:
        st.session_state.product_category = category

        with st.spinner("Analyzing consumer behavior data..."):
            st.success("Consumer behavior analysis complete!")

            st.subheader(f"📊 {category} Consumer Behavior Report")

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Market Size", "$125B")
            with col2:
                st.metric("Avg. Purchase", "$185")
            with col3:
                st.metric("Purchase Freq.", "4.2/year")
            with col4:
                st.metric("Loyalty Rate", "34%")

            tabs = st.tabs(
                [
                    "Demographics",
                    "Psychographics",
                    "Purchase Journey",
                    "Channels",
                    "Trends",
                ]
            )

            with tabs[0]:
                st.markdown("## Demographic Analysis")

                st.markdown("### Age Distribution")
                age_data = {
                    "Generation": ["Gen Z", "Millennials", "Gen X", "Boomers"],
                    "Market Share %": [18, 42, 28, 12],
                    "Avg. Spend": [85, 220, 195, 145],
                }
                st.bar_chart(age_data, x="Generation", y="Market Share %")

                st.markdown("\n### Gender Distribution")
                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown("**Female:** 58%")
                    st.markdown("- Higher average basket size")
                    st.markdown("- More brand loyal")
                    st.markdown("- Research-heavy buyers")
                with col_b:
                    st.markdown("**Male:** 42%")
                    st.markdown("- Faster purchase decisions")
                    st.markdown("- Feature-focused")
                    st.markdown("- Price-conscious")

                st.markdown("\n### Income Segmentation")
                segments = [
                    ("Premium", "$100K+", "15%", "Quality over price"),
                    ("Middle Market", "$50K-$100K", "45%", "Value-conscious"),
                    ("Economy", "$25K-$50K", "30%", "Price-driven"),
                    ("Budget", "<$25K", "10%", "Essential purchases"),
                ]
                st.markdown("| Segment | Income | Share | Priority |")
                st.markdown("|---------|--------|-------|----------|")
                for seg, income, share, priority in segments:
                    st.markdown(f"| {seg} | {income} | {share} | {priority} |")

            with tabs[1]:
                st.markdown("## Psychographic Analysis")

                st.markdown("### Values & Priorities")
                values = [
                    (
                        "Sustainability",
                        78,
                        "Environmental consciousness drives 78% of purchases",
                    ),
                    ("Quality", 85, "Premium quality expected regardless of price"),
                    ("Convenience", 72, "Ease of purchase increasingly important"),
                    (
                        "Social Proof",
                        65,
                        "Reviews and recommendations heavily influence",
                    ),
                    ("Brand Story", 58, "Authentic brand narratives resonate"),
                ]

                for value, score, desc in values:
                    st.markdown(f"### {value} ({score}%)")
                    st.progress(score / 100)
                    st.markdown(desc)
                    st.markdown("---")

                st.markdown("\n### Lifestyle Segments")
                lifestyles = [
                    (
                        "Early Adopters",
                        "12%",
                        "Seek innovation, willing to pay premium",
                    ),
                    ("Quality Seekers", "35%", "Balance quality and value"),
                    ("Pragmatists", "28%", "Functionality focused"),
                    ("Price Sensitive", "25%", "Deal hunters, brand agnostic"),
                ]
                for seg, share, desc in lifestyles:
                    st.markdown(f"- **{seg} ({share}):** {desc}")

            with tabs[2]:
                st.markdown("## Purchase Journey Analysis")

                st.markdown("### Customer Journey Map")
                stages = [
                    (
                        "Awareness",
                        "Social media, ads, word of mouth",
                        "3-5 touchpoints",
                    ),
                    (
                        "Consideration",
                        "Website research, reviews, comparisons",
                        "5-7 touchpoints",
                    ),
                    ("Decision", "Price check, checkout", "1-2 touchpoints"),
                    ("Purchase", "Transaction completion", "1 touchpoint"),
                    ("Post-Purchase", "Onboarding, support, reviews", "Ongoing"),
                ]

                for stage, touchpoints, count in stages:
                    with st.expander(f"📍 {stage}"):
                        st.markdown(f"**Channels:** {touchpoints}")
                        st.markdown(f"**Touchpoints:** {count}")

                st.markdown("\n### Key Decision Factors")
                factors = [
                    ("Price/Value", 85, "Most critical factor"),
                    ("Product Quality", 82, "Second most important"),
                    ("Brand Reputation", 68, "Trust indicator"),
                    ("Reviews/Ratings", 65, "Social proof"),
                    ("Availability", 58, "Convenience factor"),
                    ("Aesthetics", 45, "Design appeal"),
                ]
                for factor, importance, note in factors:
                    col1, col2 = st.columns([importance / 100, 1 - importance / 100])
                    with col1:
                        st.progress(importance / 100, text=f"{factor}: {importance}%")

            with tabs[3]:
                st.markdown("## Channel Preferences")

                st.markdown("### Discovery Channels")
                discovery = [
                    ("Social Media", 45, "Facebook, Instagram, TikTok"),
                    ("Search Engines", 38, "Google, Bing"),
                    ("Word of Mouth", 35, "Friends, family, colleagues"),
                    ("Retail Stores", 28, "In-person browsing"),
                    ("Email Marketing", 22, "Promotional emails"),
                ]
                st.markdown("| Channel | % Using | Top Platform |")
                st.markdown("|---------|---------|--------------|")
                for channel, pct, platform in discovery:
                    st.markdown(f"| {channel} | {pct}% | {platform} |")

                st.markdown("\n### Purchase Channels")
                purchase_channels = [
                    ("E-commerce Website", "55%", "Direct, branded experience"),
                    ("Marketplace (Amazon)", "28%", "Convenience, reviews"),
                    ("Retail Store", "12%", "Immediate gratification"),
                    ("Mobile App", "5%", "Loyalty program members"),
                ]
                for channel, share, note in purchase_channels:
                    st.markdown(f"- **{channel}:** {share} - {note}")

                st.markdown("\n### Channel by Generation")
                channel_gen = {
                    "Generation": ["Gen Z", "Millennials", "Gen X", "Boomers"],
                    "Mobile": [85, 72, 55, 35],
                    "Desktop": [15, 28, 45, 55],
                    "In-Store": [20, 25, 35, 50],
                }
                st.bar_chart(channel_gen, x="Generation")

            with tabs[4]:
                st.markdown("## Emerging Trends")

                st.markdown("### 2024 Consumer Trends")
                trends = [
                    (
                        "Sustainable Shopping",
                        "78% willing to pay more for sustainable products",
                        "Opportunity for eco-friendly positioning",
                    ),
                    (
                        "Social Commerce",
                        "55% have purchased through social media",
                        "Invest in social selling",
                    ),
                    (
                        "Personalization",
                        "72% expect personalized experiences",
                        "AI-driven recommendations",
                    ),
                    (
                        "Experiential Retail",
                        "63% prefer brands that offer experiences",
                        "Blend online/offline experiences",
                    ),
                    (
                        "Subscription Models",
                        "45% subscribed to at least one service",
                        "Recurring revenue opportunity",
                    ),
                ]

                for trend, stat, action in trends:
                    with st.expander(f"📈 {trend}"):
                        st.markdown(f"**Statistic:** {stat}")
                        st.markdown(f"**Action:** {action}")

                st.markdown("\n### Forecast (Next 12 Months)")
                st.markdown("""
                - Continued shift to online purchasing
                - Increased demand for transparency
                - Rise of micro-moments and impulse purchases
                - Greater emphasis on community building
                - Integration of AR/VR in shopping experience
                """)

                st.markdown("\n### Strategic Recommendations")
                recommendations = [
                    "Omnichannel presence is essential",
                    "Invest in sustainability messaging",
                    "Leverage user-generated content",
                    "Implement personalized marketing",
                    "Build community around brand",
                ]
                for rec in recommendations:
                    st.markdown(f"- {rec}")

if st.button("Clear"):
    st.session_state.clear()
    st.rerun()
