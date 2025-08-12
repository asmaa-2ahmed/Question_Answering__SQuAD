import streamlit as st
from typing import Dict, Any

def display_answer(result: Dict[str, Any]):
    """Cleaner answer display layout"""
    st.markdown("""
    <style>
        .answer-container {
            background-color: var(--secondary-background-color);
            border-radius: 10px;
            padding: 1.25rem;
            margin: 0.75rem 0;
            border-left: 4px solid var(--primary-color);
            box-shadow: 0 2px 5px rgba(0,0,0,0.08);
        }
        .answer-title {
            font-size: 1.15rem;
            font-weight: 600;
            margin-bottom: 0.65rem;
            color: var(--text-color);
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }
        .answer-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 0.5rem;
            font-size: 1.05rem;
        }
        .confidence-badge {
            background-color: rgba(79, 139, 249, 0.15);
            color: var(--primary-color);
            padding: 0.3rem 0.8rem;
            border-radius: 12px;
            font-size: 0.85rem;
            font-weight: 500;
        }
        .position-text {
            margin-top: 0.75rem;
            color: var(--text-secondary-color);
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="answer-container">
        <div class="answer-title">
            <span>✅</span><span>Answer</span>
        </div>
        <div class="answer-content" style="color: var(--text-color);">
            <span>{result['answer']}</span>
            <span class="confidence-badge">Confidence: {result['score']:.0%}</span>
        </div>
        <div class="position-text">
            <span>📍</span>
            <span>Position: {result['start']}-{result['end']}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def highlight_context(context: str, start: int, end: int):
    """Context highlighter - removed trailing space after heading and removed extra streamlit margins"""
    st.markdown("""
    <style>
        .context-wrapper { margin-top: 0 !important; padding: 0; }
        .context-heading {
            margin: 0 !important;
            padding: 0 !important;
            font-weight: 600;
            display: block;
        }
        .context-container {
            background-color: var(--background-color);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 1rem;
            margin-top: 0 !important;
            white-space: pre-wrap;
            color: var(--text-color);
            line-height: 1.6;
        }
        .highlight {
            background-color: #FFEE58;
            color: #000;
            padding: 0.15em 0.3em;
            border-radius: 0.35em;
            font-weight: 600;
            box-shadow: 0 0 2px rgba(0,0,0,0.2);
        }
    </style>
    """, unsafe_allow_html=True)

    # Render heading + container in a single block to avoid extra Streamlit spacing
    st.markdown(f"""
    <div class="context-wrapper">
        <div class="context-heading">Context with highlighted answer:</div>
        <div class="context-container">
            {context[:start]}
            <span class="highlight">{context[start:end]}</span>
            {context[end:]}
        </div>
    </div>
    """, unsafe_allow_html=True)

def display_results(context: str, result: Dict[str, Any]):
    try:
        display_answer(result)
        highlight_context(context, result['start'], result['end'])
    except Exception as e:
        st.error(f"Error displaying results: {str(e)}")
