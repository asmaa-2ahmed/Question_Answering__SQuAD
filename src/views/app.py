import streamlit as st
from src.inference import answer_question
from src.schemas import QARequest
from src.views.components.header import show_header
from src.views.components.sidebar import show_sidebar
from src.views.components.input_form import get_user_inputs
from src.views.components.answer_display import display_results

def handle_qa_request(context: str, question: str):
    """Process QA request and display results"""
    try:
        if not context.strip() or not question.strip():
            st.error("Please provide both context and question")
            return

        result = answer_question(question, context)
        display_results(context, result)

    except Exception as e:
        st.error(f"Error processing request: {str(e)}")

def main():
    """Main application flow with blue focus borders"""
    st.set_page_config(
        page_title="QA System",
        page_icon="🔍",
        layout="centered"
    )
    
    # Add global styles
        # Global typography styles
    st.markdown("""
    <style>
        /* Set a consistent font for everything */
        html, body, [class*="css"]  {
            font-family: 'Segoe UI', 'Roboto', sans-serif !important;
        }

        /* Adjust main page header size */
        h1, .main-title {
            font-size: 1.8rem !important; /* smaller than Streamlit's default */
            font-weight: 700 !important;
            margin-bottom: 0.5rem !important;
        }

        /* Subtitle or description under header */
        h2, h3, .subheader {
            font-size: 1.1rem !important;
            font-weight: 500 !important;
            margin-top: 0.25rem !important;
        }

        /* Standard text size for paragraphs and markdown */
        p, div, span, label {
            font-size: 1rem !important;
            line-height: 1.5 !important;
        }
    </style>
    """, unsafe_allow_html=True)

    
    show_header()
    show_sidebar()
    
    context, question, submitted = get_user_inputs()
    if submitted and context and question:
        handle_qa_request(context, question)

