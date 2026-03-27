import streamlit as st

st.set_page_config(page_title="Technical Documentation Research", page_icon="📚")

st.title("📚 Technical Documentation Research")
st.markdown("Research and analyze technical documentation")

if "tech_topic" not in st.session_state:
    st.session_state.tech_topic = ""

col1, col2 = st.columns([2, 1])
with col1:
    tech_topic = st.text_input(
        "Technology/Framework",
        value=st.session_state.tech_topic,
        placeholder="e.g., React, Docker, GraphQL",
    )
with col2:
    experience = st.selectbox(
        "Your Experience", ["Beginner", "Intermediate", "Advanced"]
    )

st.markdown("### Documentation Type")
doc_types = st.multiselect(
    "Types to explore",
    ["Getting Started", "API Reference", "Tutorials", "Best Practices", "Architecture"],
    default=["Getting Started", "Tutorials", "Best Practices"],
)

if st.button("Research Documentation", type="primary"):
    if tech_topic:
        st.session_state.tech_topic = tech_topic

        with st.spinner("Analyzing documentation..."):
            st.success("Documentation research complete!")

            st.subheader(f"📖 {tech_topic} Documentation Overview")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Version", "v18.x")
            with col2:
                st.metric("Last Updated", "2 weeks ago")
            with col3:
                st.metric("Coverage", "Excellent")

            tabs = st.tabs(
                [
                    "Overview",
                    "Getting Started",
                    "API Reference",
                    "Architecture",
                    "Best Practices",
                ]
            )

            with tabs[0]:
                st.markdown("## Documentation Overview")

                st.markdown(f"""
                ### About {tech_topic}
                {tech_topic} is a modern technology designed to build scalable and efficient applications.
                It provides developers with powerful tools and abstractions for rapid development.

                ### Key Characteristics
                - **Type:** Modern development framework
                - **Primary Use Cases:** Web development, API building, microservices
                - **Learning Curve:** {experience}-friendly
                - **Community Size:** Large and active
                - **Job Market Demand:** High
                """)

                st.markdown("\n### Documentation Structure")
                structure = [
                    ("Getting Started", "Quick installation and first application"),
                    ("Core Concepts", "Fundamental principles and patterns"),
                    ("API Reference", "Complete method and function documentation"),
                    (" Tutorials", "Step-by-step guides for common tasks"),
                    ("Migration Guide", "Upgrade from previous versions"),
                ]
                for section, desc in structure:
                    st.markdown(f"- **{section}:** {desc}")

            with tabs[1]:
                st.markdown("## Getting Started Guide")

                st.markdown("### Installation")
                st.code(
                    "npm install " + tech_topic.lower().replace(" ", "-"),
                    language="bash",
                )

                st.markdown("\n### Quick Start Example")
                example_code = f"""import {{ Component }} from '{tech_topic.lower()}';

// Create your first component
const App = () => {{
  return (
    <div>
      <h1>Welcome to {tech_topic}!</h1>
      <p>Get started with your first application.</p>
    </div>
  );
}};

export default App;"""
                st.code(example_code, language="javascript")

                st.markdown("\n### Prerequisites")
                prerequisites = [
                    "Node.js 18.x or higher",
                    "npm or yarn package manager",
                    "Basic JavaScript knowledge",
                    "Familiarity with web development",
                ]
                for prereq in prerequisites:
                    st.markdown(f"- {prereq}")

                st.markdown("\n### Next Steps")
                st.markdown("""
                1. Complete the "Hello World" tutorial
                2. Learn about core components
                3. Build your first feature
                4. Explore the example projects
                """)

            with tabs[2]:
                st.markdown("## API Reference")

                st.markdown("### Core APIs")

                apis = [
                    ("Component", "Base class for UI components", "Core"),
                    ("useState", "State management hook", "Hooks"),
                    ("useEffect", "Side effect handler", "Hooks"),
                    ("createContext", "Context creation", "Advanced"),
                    ("render", "Render component to DOM", "Core"),
                ]

                for name, desc, category in apis:
                    with st.expander(f"📦 {name} ({category})"):
                        st.markdown(f"**Description:** {desc}")
                        st.markdown(
                            f"**Usage:** `import {{ {name} }} from '{tech_topic.lower()}'`"
                        )

                st.markdown("\n### Common Patterns")
                patterns = [
                    (
                        "Component Composition",
                        "Build complex UIs from simple components",
                    ),
                    ("Provider Pattern", "Share state across components"),
                    ("Higher-Order Components", "Enhance existing components"),
                    ("Custom Hooks", "Extract and reuse stateful logic"),
                ]
                for pattern, desc in patterns:
                    st.markdown(f"- **{pattern}:** {desc}")

            with tabs[3]:
                st.markdown("## Architecture Guide")

                st.markdown("### System Architecture")
                st.markdown("""
                ```
                ┌─────────────────────────────────────┐
                │         Application Layer          │
                ├─────────────────────────────────────┤
                │         Business Logic            │
                ├─────────────────────────────────────┤
                │         Data Layer                 │
                ├─────────────────────────────────────┤
                │         Infrastructure             │
                └─────────────────────────────────────┘
                ```
                """)

                st.markdown("\n### Key Principles")
                principles = [
                    ("Modularity", "Separate concerns into distinct modules"),
                    ("Reusability", "Build components that can be reused"),
                    ("Testability", "Design for easy testing"),
                    ("Performance", "Optimize for speed and efficiency"),
                ]
                for principle, desc in principles:
                    st.markdown(f"### {principle}")
                    st.markdown(desc)
                    st.markdown("---")

                st.markdown("\n### Design Patterns")
                patterns = [
                    ("Container/Presentational", "Separate logic from UI"),
                    ("Observer", "Handle reactive updates"),
                    ("Factory", "Create objects without specifying exact class"),
                ]
                for name, desc in patterns:
                    st.markdown(f"- **{name}:** {desc}")

            with tabs[4]:
                st.markdown("## Best Practices")

                st.markdown("### Code Organization")
                st.markdown("""
                ```javascript
                src/
                ├── components/    # Reusable UI components
                ├── hooks/         # Custom React hooks
                ├── utils/         # Utility functions
                ├── services/      # API calls and external services
                └── contexts/     # React contexts
                ```
                """)

                st.markdown("\n### Performance Tips")
                tips = [
                    "Use React.memo() for expensive components",
                    "Implement code splitting with lazy loading",
                    "Avoid unnecessary re-renders with useMemo/useCallback",
                    "Optimize images and assets",
                    "Use production build for deployment",
                ]
                for tip in tips:
                    st.markdown(f"- {tip}")

                st.markdown("\n### Security Best Practices")
                security = [
                    "Validate all user inputs",
                    "Use environment variables for secrets",
                    "Implement proper authentication",
                    "Keep dependencies updated",
                    "Use HTTPS in production",
                ]
                for item in security:
                    st.markdown(f"- {item}")

                st.markdown("\n### Testing Strategy")
                st.markdown("""
                - **Unit Tests:** Test individual functions and components
                - **Integration Tests:** Test component interactions
                - **E2E Tests:** Test complete user flows
                - **Coverage Target:** 80%+
                """)

if st.button("Clear"):
    st.session_state.clear()
    st.rerun()
