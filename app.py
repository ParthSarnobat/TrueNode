import os
import streamlit as st
from dotenv import load_dotenv
from UI.layout import render_sidebar, render_main_content

# Load environment variables from .env
load_dotenv()

# Page configuration (Note: st.set_page_config must be called in layout.py or here, 
# keeping it here for primary entry point definition)
st.set_page_config(
    page_title="TrueNode | Research Intelligence",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Render UI components from layout module
    uploaded_files, run_button, api_key_input = render_sidebar()
    agent_status, summary_box, graph_box, audio_box = render_main_content()
    
    # Handle execution trigger
    if run_button:
        # Input Validation
        if not uploaded_files:
            st.sidebar.error("⚠️ Please upload at least one PDF research paper to proceed.")
            return
            
        # Retrieve API key fallback logic
        active_api_key = api_key_input or os.getenv("NEBIUS_API_KEY")
        if not active_api_key:
            st.sidebar.error("🔑 API Key missing! Please enter your Nebius key or set it in .env")
            return

        # Modernized Progressive Status Container for LangGraph Agent Steps
        with agent_status.status("🚀 Running TrueNode Pipeline...", expanded=True) as status:
            st.write("📂 Parsing uploaded PDF research papers...")
            # TODO: Integrate Phase 2 (Ingestion & ChromaDB) here
            
            st.write("🤖 Initializing LangGraph & invoking Nemotron extraction agents...")
            # TODO: Integrate Phase 3 (Agents) here
            
            st.write("🌐 Constructing cross-paper relationship topology...")
            # TODO: Integrate graph synthesis here
            
            status.update(
                label="✨ Pipeline execution complete successfully!", 
                state="complete", 
                expanded=False
            )
        
        # Polished Success Feedback & Mock Outputs
        summary_box.success("🎯 Extraction and synthesis completed successfully! (Mock Output)")
        
        # Render a sleek Mermaid relationship diagram inside a styled card block
        graph_box.markdown("""
            ```mermaid
            graph TD
                classDef primary fill:#1f6feb,stroke:#388bfd,stroke-width:2px,color:#fff;
                classDef secondary fill:#21262d,stroke:#30363d,stroke-width:2px,color:#c9d1d9;
                
                A[Paper 1: Core Methodology] -->|Builds upon| B[Paper 2: Baseline Findings]
                B -->|Validates tensor architecture| C[Paper 3: Scaled Evaluation]
                A -->|Extends optimization| C
                
                class A,C primary;
                class B secondary;
            ```
        """)
        
        # Placeholder audio simulation feedback
        audio_box.info("🎧 NVIDIA Sonic podcast overview generated. (Audio player widget placeholder)")

if __name__ == "__main__":
    main()