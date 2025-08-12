import streamlit as st

def show_header():
    """Display the application header"""
    st.markdown("""
    <div class="header" style="text-align: center; margin-bottom: 2rem;">
        <h1 style="color: #4F8BF9;">🔍 Question Answering System</h1>
        <p style="color: #666;">Powered by fine-tuned DistilBERT model</p>
    </div>
    """, unsafe_allow_html=True)

# without the color, 

# import streamlit as st

# def show_header():
#     """Display the application header with emojis"""
#     st.markdown("""
#     <div style="text-align: center; margin-bottom: 2rem;">
#         <h1>🔍 Question Answering System</h1>
#         <p>Powered by fine-tuned DistilBERT model</p>
#     </div>
#     """, unsafe_allow_html=True)