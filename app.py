"""
Medical Trend Analytics
Dedicated application for category-specific medical trend analysis.
"""
import streamlit as st
from datetime import datetime
import os
import sys
import markdown

# Local imports
from core.collector import PaperCollector
from core.trend_analyzer import TrendAnalyzer
from config.journals import get_journals_by_category

# ==========================================
# Helper Functions
# ==========================================
def get_secret(key, default=None):
    """Safely get secret from st.secrets or environment variables."""
    # First check env vars (good for dev/docker)
    val = os.environ.get(key)
    if val:
        return val
    # Then check st.secrets
    try:
        return st.secrets.get(key, default)
    except:
        return default

def clear_analysis_cache():
    """Clear all analysis results from session state."""
    keys_to_clear = [k for k in st.session_state.keys() if k.startswith("result_") or k.startswith("papers_")]
    for k in keys_to_clear:
        del st.session_state[k]

# ==========================================
# Main App
# ==========================================
def main():
    st.set_page_config(
        page_title="Medical Trend Analytics",
        page_icon="📈",
        layout="wide"
    )

    st.title("📈 Medical Trend Analytics")
    st.markdown("Category-specific insights from top medical journals.")

    # ------------------------------------------
    # Sidebar Configuration
    # ------------------------------------------
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # Model
        default_model = get_secret("OLLAMA_MODEL", "gpt-oss:120b")
        model_name = st.text_input("Ollama Model", value=default_model)
        
        # Time Period
        months_back = st.selectbox(
            "Time Period",
            options=[3, 6, 12],
            format_func=lambda x: f"Last {x} months",
            index=0
        )
        
        # Cache Invalidation Logic
        if 'last_months_back' not in st.session_state:
            st.session_state.last_months_back = months_back
        elif st.session_state.last_months_back != months_back:
            clear_analysis_cache()
            st.session_state.last_months_back = months_back
            st.toast("Time period changed. Analysis cache cleared.", icon="🔄")

        st.divider()
        
        # API Key Status
        ollama_api_key = get_secret("OLLAMA_API_KEY")
        st.subheader("🔑 Status")
        if ollama_api_key:
            st.success("✅ API Key Loaded")
            st.caption("Ready for Cloud Inference")
        else:
            st.warning("⚠️ No API Key Detected")
            st.caption("Local Ollama will be used (if available), or ensure OLLAMA_API_KEY is in secrets.toml")
            
        st.divider()
        st.info("Select a category tab to begin analysis.")

    # ------------------------------------------
    # Main Content: Tabs
    # ------------------------------------------
    categories = get_journals_by_category()
    
    # Create tabs
    tab_names = list(categories.keys())
    # Add an Overview tab? Or just categories. Let's stick to categories + Summary
    # The requirement was "Tabs based dynamically generated".
    
    tabs = st.tabs([f"📌 {name}" for name in tab_names])
    
    for i, (category, journals) in enumerate(categories.items()):
        with tabs[i]:
            st.header(f"{category} Analysis")
            
            col_left, col_right = st.columns([1, 2])
            
            with col_left:
                st.subheader("Select Journals")
                with st.container(border=True):
                    # Checkboxes for journals
                    selected_journals = []
                    
                    # "Select All" functionality within the form context is tricky with dynamic widgets,
                    # so we'll default all to Checked.
                    
                    for journal in journals:
                        # Use a unique key for each checkbox
                        if st.checkbox(f"**{journal['name']}**", value=True, key=f"chk_{category}_{journal['name']}"):
                            selected_journals.append(journal)
                    
                    if not selected_journals:
                        st.warning("Select at least one journal.")
                
                # Analyze Button
                analyze_btn = st.button(
                    f"🚀 Analyze {category} Trends", 
                    key=f"btn_analyze_{category}",
                    type="primary",
                    use_container_width=True,
                    disabled=(not selected_journals)
                )

            with col_right:
                result_key = f"result_{category}"
                papers_key = f"papers_{category}"
                
                if analyze_btn and selected_journals:
                    # Execute Analysis
                    collector = PaperCollector()
                    all_papers = []
                    
                    # 1. Fetch
                    with st.spinner(f"📡 Fetching papers from {len(selected_journals)} journals ({months_back} months)..."):
                        progress_bar = st.progress(0)
                        for idx, journal in enumerate(selected_journals):
                            fetched = collector.fetch_papers(journal["url"], months_back, max_papers=20)
                            for p in fetched:
                                p['source'] = journal['name']
                                all_papers.append(p)
                            progress_bar.progress((idx + 1) / len(selected_journals))
                        progress_bar.empty()
                    
                    if not all_papers:
                        st.error("No papers found in this period.")
                    else:
                        st.session_state[papers_key] = all_papers
                        
                        # 2. Analyze
                        with st.spinner("🧠 Asking Ollama Cloud to analyze trends..."):
                            try:
                                # Instantiate analyzer (API key handled internally by common_lib)
                                analyzer = TrendAnalyzer(model_name=model_name)
                                trend_text = analyzer.analyze_trends(all_papers)
                                st.session_state[result_key] = trend_text
                            except Exception as e:
                                st.error(f"Analysis failed: {str(e)}")

                # Display Results
                if result_key in st.session_state:
                    st.success(f"Analysis Complete! Based on {len(st.session_state.get(papers_key, []))} papers.")
                    
                    with st.container(border=True):
                        st.markdown("### 📊 AI Trend Report")
                        st.markdown(st.session_state[result_key])
                        
                    # Show papers source list in expander
                    with st.expander("📚 View Source Papers"):
                        papers = st.session_state.get(papers_key, [])
                        for p in papers[:50]: # Limit display
                            st.markdown(f"- [{p['title']}]({p['link']}) ({p.get('published','')}) - *{p.get('source')}*")
                        if len(papers) > 50:
                            st.caption(f"...and {len(papers)-50} more.")
                
                elif not analyze_btn:
                    st.info("👈 Select journals and click Analyze to generate a report.")

if __name__ == "__main__":
    main()
