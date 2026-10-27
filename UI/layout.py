import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="TrueNode: Research Graph & Synthesis Engine",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- MODERN UI STYLING (CSS) ---
def load_custom_css():
    st.markdown("""
        <style>
            /* Global Theme Adjustments */
            .main {
                background-color: #0e1117;
            }
            
            /* Custom Card Containers */
            .stCard {
                background-color: #161b22;
                border: 1px solid #30363d;
                padding: 1.25rem;
                border-radius: 12px;
                margin-bottom: 1rem;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }

            /* Headers & Typography */
            h1, h2, h3 {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                letter-spacing: -0.02em;
            }
            
            /* Sidebar Styling */
            [data-testid="stSidebar"] {
                background-color: #0b0f19;
                border-right: 1px solid #1f293d;
            }

            /* Buttons */
            .stButton button {
                border-radius: 8px;
                font-weight: 600;
                transition: all 0.2s ease-in-out;
            }
            .stButton button:hover {
                transform: translateY(-1px);
                box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
            }
        </style>
    """, unsafe_allow_html=True)

def render_sidebar():
    """Renders a sleek, modern sidebar for API key verification and multiple PDF uploads."""
    st.sidebar.markdown("### 🎛️ Control Panel")
    st.sidebar.markdown("---")
    
    st.sidebar.markdown("#### 🔑 Configuration")
    api_key_input = st.sidebar.text_input(
        "Nebius API Key", 
        type="password", 
        placeholder="sk-...",
        help="Enter your Nebius inference key if not loaded from .env"
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("#### 📁 Document Ingestion")
    uploaded_files = st.sidebar.file_uploader(
        "Upload Research Papers", 
        type=["pdf"], 
        accept_multiple_files=True,
        help="Upload one or more PDFs to synthesize and map."
    )
    
    # Show file count badge if files are uploaded
    if uploaded_files:
        st.sidebar.success(f"📎 {len(uploaded_files)} paper(s) ready for ingestion.")

    st.sidebar.markdown("---")
    st.sidebar.markdown("#### ⚡ Execution")
    run_button = st.sidebar.button(
        "🚀 Run Analysis Pipeline", 
        type="primary", 
        use_container_width=True
    )
    
    return uploaded_files, run_button, api_key_input

def render_main_content():
    """Renders the main layout area with card-like sections for logs, graphs, and summaries."""
    load_custom_css()
    
    # Hero Header Section
    st.markdown("""
        <div style="padding: 1rem 0 2rem 0;">
            <h1 style="margin-bottom: 0.2rem; font-size: 2.25rem;">🔬 TrueNode <span style="color: #3b82f6; font-size: 1.25rem; font-weight: 400;">v2.0</span></h1>
            <p style="color: #8b949e; font-size: 1.1rem; margin-top: 0;">Autonomous research paper extraction, cross-paper relationship mapping, and plain-language summarization.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Create main layout columns with balanced spacing
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        # Agent Brain Logs Container
        with st.container():
            st.markdown("### 🧠 Agent Brain Logs")
            st.markdown("<p style='color: #8b949e; font-size: 0.85rem; margin-top: -10px;'>Real-time LangGraph execution steps</p>", unsafe_allow_html=True)
            agent_status_placeholder = st.empty()
            # Default state styling box
            agent_status_placeholder.info("🔄 Pipeline idle. Awaiting trigger...")
        
        st.markdown("<div style='margin: 1.5rem 0;'></div>", unsafe_allow_html=True)
        
        # Final Text Summary Container
        with st.container():
            st.markdown("### 📑 Final Text Summary")
            st.markdown("<p style='color: #8b949e; font-size: 0.85rem; margin-top: -10px;'>Synthesized insights & key takeaways</p>", unsafe_allow_html=True)
            summary_placeholder = st.empty()
            summary_placeholder.info("⏳ Awaiting pipeline execution to generate plain-language summary...")

    with col2:
        # Research Relationship Graph Container
        with st.container():
            st.markdown("### 📊 Research Relationship Graph")
            st.markdown("<p style='color: #8b949e; font-size: 0.85rem; margin-top: -10px;'>Cross-paper conceptual dependency map</p>", unsafe_allow_html=True)
            graph_placeholder = st.empty()
            graph_placeholder.info("🌐 Mermaid relationship graph will appear here after analysis.")
        
        st.markdown("<div style='margin: 1.5rem 0;'></div>", unsafe_allow_html=True)
        
        # Audio Narrator Container
        with st.container():
            st.markdown("### 🔊 Audio Narrator")
            st.markdown("<p style='color: #8b949e; font-size: 0.85rem; margin-top: -10px;'>NVIDIA Sonic podcast-style overview</p>", unsafe_allow_html=True)
            audio_placeholder = st.empty()
            audio_placeholder.text("🎧 Audio summary player will initialize post-run.")

    return agent_status_placeholder, summary_placeholder, graph_placeholder, audio_placeholder

# --- MAIN EXECUTION APP LOOP ---
if __name__ == "__main__":
    files, run, api_key = render_sidebar()
    agent_status, summary, graph, audio = render_main_content()