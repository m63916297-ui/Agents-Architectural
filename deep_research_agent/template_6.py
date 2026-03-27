import streamlit as st

st.set_page_config(page_title="SEO Content Research", page_icon="🔍")

st.title("🔍 SEO Content Research Tool")
st.markdown("Research and optimize content for search engines")

if "keyword" not in st.session_state:
    st.session_state.keyword = ""

col1, col2 = st.columns([2, 1])
with col1:
    keyword = st.text_input(
        "Primary Keyword",
        value=st.session_state.keyword,
        placeholder="e.g., best coffee shops",
    )
with col2:
    location = st.selectbox(
        "Target Location", ["Global", "United States", "Europe", "Specific Country"]
    )

st.markdown("### Additional Keywords (comma-separated)")
related_keywords = st.text_input(
    "Related Keywords", placeholder="cafe, espresso, coffee near me"
)

if st.button("Research Keywords", type="primary"):
    if keyword:
        st.session_state.keyword = keyword

        with st.spinner("Analyzing keyword data..."):
            st.success("Research complete!")

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Search Volume", "18,100/mo")
            with col2:
                st.metric("Difficulty", "42/100")
            with col3:
                st.metric("CPC", "$2.45")
            with col4:
                st.metric("Trend", "📈 Rising")

            tabs = st.tabs(
                [
                    "Keyword Analysis",
                    "Content Brief",
                    "Competitor Analysis",
                    "SERP Features",
                    "Link Building",
                ]
            )

            with tabs[0]:
                st.markdown("## Keyword Analysis")

                st.markdown("### Primary Keyword Metrics")
                metrics_data = {
                    "Metric": [
                        "Search Volume",
                        "Competition",
                        "Trend (12mo)",
                        "Intl. Volume",
                    ],
                    "Value": ["18,100", "Medium", "+23%", "45,200"],
                }
                st.dataframe(metrics_data, use_container_width=True)

                st.markdown("\n### Related Keywords")
                related = [
                    ("coffee shops near me", "12,100", "High", "88%"),
                    ("best coffee near me", "8,800", "Medium", "72%"),
                    ("local coffee shops", "6,600", "Low", "65%"),
                    ("coffee cafe", "5,400", "Medium", "58%"),
                    ("specialty coffee", "4,400", "Low", "45%"),
                ]

                st.markdown("| Keyword | Volume | Competition | Relevance |")
                st.markdown("|---------|--------|-------------|-----------|")
                for kw, vol, comp, rel in related:
                    st.markdown(f"| {kw} | {vol} | {comp} | {rel} |")

                st.markdown("\n### Question Keywords")
                questions = [
                    "what is the best coffee shop near me",
                    "how to find good coffee shops",
                    "why are coffee shops popular",
                    "what makes a good coffee shop",
                ]
                for q in questions:
                    st.markdown(f"- {q}")

            with tabs[1]:
                st.markdown("## Content Brief")

                st.markdown("### Recommended Structure")
                structure = """
                **H1: Best Coffee Shops Near You [2024 Ultimate Guide]**
                
                **Introduction** (150 words)
                - Hook: "Looking for the perfect cup of coffee?"
                - Brief mention of what makes a great coffee shop
                - What readers will learn
                
                **H2: What to Look for in a Great Coffee Shop** (300 words)
                - Coffee quality
                - Atmosphere
                - Service
                - Price point
                
                **H2: Top 10 Best Coffee Shops in [Your City]** (800 words)
                - Include ratings, addresses, hours
                - Photos (if applicable)
                - Unique selling points
                
                **H2: How to Find Hidden Gem Coffee Shops** (400 words)
                - Local recommendations
                - Online reviews
                - Social media tips
                
                **H2: FAQs About Coffee Shops** (300 words)
                """
                st.code(structure, language="markdown")

                st.markdown("\n### SEO Recommendations")
                recommendations = [
                    (
                        "Title Tag",
                        "Best Coffee Shops Near You | Top 10 Local Cafes [2024]",
                        "60 chars",
                    ),
                    (
                        "Meta Description",
                        "Discover the best coffee shops near you. Expert reviews of top-rated cafes, hidden gems, and must-try spots in your area.",
                        "155 chars",
                    ),
                    ("URL Slug", "/best-coffee-shops-near-me", ""),
                    ("Headers", "Use H1, H2, H3 hierarchy naturally", ""),
                ]

                for elem, content, note in recommendations:
                    st.markdown(f"**{elem}:** {content}")
                    if note:
                        st.caption(note)

            with tabs[2]:
                st.markdown("## Competitor Analysis")

                competitors = [
                    (
                        "blog.coffeenation.com",
                        "DA: 45",
                        "1,200 words",
                        "How to Brew",
                        "Top 10",
                    ),
                    (
                        "www.coffeeshopguide.com",
                        "DA: 52",
                        "800 words",
                        "Reviews Focus",
                        "Lists",
                    ),
                    (
                        "thecoffeeconfidential.com",
                        "DA: 38",
                        "1,500 words",
                        "Quality Focus",
                        "Guide",
                    ),
                ]

                st.markdown("| Domain | Authority | Length | Focus | Type |")
                st.markdown("|--------|-----------|--------|-------|------|")
                for domain, da, length, focus, typ in competitors:
                    st.markdown(f"| {domain} | {da} | {length} | {focus} | {typ} |")

                st.markdown("\n### Content Gap Opportunities")
                st.markdown("""
                - **Interactive maps** showing coffee shop locations
                - **Filter by specialty** (espresso, pour-over, cold brew)
                - **Price comparisons** across different shops
                - **User-submitted reviews** and photos
                - **Seasonal guides** (best coffee in summer/winter)
                """)

            with tabs[3]:
                st.markdown("## SERP Features")

                st.markdown("### Current Ranking Features")
                features = [
                    (
                        "People Also Ask",
                        "High opportunity",
                        "Appears in 65% of results",
                    ),
                    ("Local Pack", "Essential", "Maps + 3 listings"),
                    ("Reviews", "Important", "Star ratings shown"),
                    ("Images", "Recommended", "Featured snippets"),
                    ("Videos", "Optional", "1-2 minute clips"),
                ]

                for feature, priority, note in features:
                    emoji = (
                        "🔴"
                        if priority == "Essential"
                        else "🟡"
                        if "High" in priority
                        else "🟢"
                    )
                    st.markdown(f"{emoji} **{feature}** - {priority}")
                    st.caption(note)

                st.markdown("\n### Featured Snippet Opportunities")
                st.markdown("""
                Target queries for featured snippets:
                - "how to choose a coffee shop"
                - "what is the average price of coffee"
                - "difference between espresso and coffee"
                """)

            with tabs[4]:
                st.markdown("## Link Building Strategy")

                st.markdown("### Internal Linking")
                st.markdown("""
                Link from:
                - Coffee brewing guides
                - Café reviews
                - Coffee bean comparisons
                - Café hopping city guides
                """)

                st.markdown("\n### External Linking Opportunities")
                outreach = [
                    (
                        "Local business associations",
                        "Medium",
                        "Coffee shop partnerships",
                    ),
                    ("Food bloggers", "High", "Guest posts, reviews"),
                    ("City guides", "High", "Directory listings"),
                    ("Coffee industry sites", "Medium", "Resource pages"),
                ]

                for target, priority, approach in outreach:
                    st.markdown(f"- **{target}** ({priority}): {approach}")

if st.button("Clear"):
    st.session_state.clear()
    st.rerun()
