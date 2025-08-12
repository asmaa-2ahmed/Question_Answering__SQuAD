import streamlit as st

def _clear_inputs():
    st.session_state['context_input'] = ""
    st.session_state['question_input'] = ""

def get_user_inputs():
    """Display input form with styled native buttons, working Clear, and hint placeholders."""
    st.markdown("""
    <style>
        .stTextArea textarea,
        .stTextInput input,
        textarea,
        input {
            border: 1px solid var(--border-color) !important;
            box-shadow: none !important;
            outline: none !important;
            margin-bottom: 0 !important;
            background-clip: padding-box;
        }
        .stTextArea textarea:focus,
        .stTextInput input:focus,
        textarea:focus,
        input:focus {
            border: 1px solid #1e90ff !important;
            box-shadow: 0 0 0 3px rgba(30, 144, 255, 0.12) !important;
            outline: none !important;
        }
        .stTextArea textarea:invalid,
        .stTextInput input:invalid,
        textarea:invalid,
        input:invalid {
            box-shadow: none !important;
            border-color: var(--border-color) !important;
        }
        input:-webkit-autofill,
        textarea:-webkit-autofill {
            -webkit-box-shadow: 0 0 0px 1000px var(--background-color) inset !important;
            box-shadow: 0 0 0px 1000px var(--background-color) inset !important;
        }
        .stButton > button {
            border-radius: 8px !important;
            padding: 0.55rem 0.9rem !important;
            font-weight: 600 !important;
            box-shadow: 0 2px 6px rgba(0,0,0,0.12) !important;
        }
        .stButton > button:first-child {
            background: linear-gradient(135deg,#1E90FF 0%,#00BFFF 100%) !important;
            color: white !important;
            border: none !important;
        }
        .stButton > button:first-child:hover {
            transform: translateY(-1px);
        }
        .stColumns > div:nth-child(2) .stButton > button {
            background: transparent !important;
            color: var(--text-color) !important;
            border: 1px solid var(--border-color) !important;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("📝 **Context**")
    context = st.text_area(
        "Paste your text here...",
        height=150  ,
        label_visibility="collapsed",
        key='context_input',
        placeholder="e.g., Hugging Face is a company that develops tools for building applications using machine learning."
    )

    st.markdown("❓ **Your Question**")
    question = st.text_input(
        "What would you like to know?",
        label_visibility="collapsed",
        key='question_input',
        placeholder="e.g., What does Hugging Face develop?"
    )

    col1, col2 = st.columns([2, 1])
    with col1:
        submitted = st.button("Get Answer 🚀", use_container_width=True, key="get_answer")
    with col2:
        st.button("Clear ♻️", use_container_width=True, on_click=_clear_inputs, key="clear_btn")

    return context, question, submitted
