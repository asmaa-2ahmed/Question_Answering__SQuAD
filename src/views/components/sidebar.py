import streamlit as st

def show_sidebar():
    """Display sidebar content with usage instructions"""
    with st.sidebar:
        st.markdown("## ℹ️ About ")
        st.markdown("""
        This QA system extracts answers from text using AI.
        
        **How to use:**
        1. 📝 Paste your text in the context box
        2. ❓ Ask a question about the text
        3. ✅ Get accurate answers with positions
        
        **Tips:**
        - Longer contexts work better
        - Be specific with questions
        - Check answer positions
        """)