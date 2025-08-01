import streamlit as st
import sys
import os
from streamlit.components.v1 import html

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import agent, llm, classify_intent

st.set_page_config(
    page_title="Agentic AI Assistant",
    layout="centered"
)

st.markdown("""
    <style>
        body {
            background-color: #f9f9f9;
        }
        .stChatMessage {
            border-radius: 12px;
            padding: 12px;
            margin-bottom: 10px;
            background-color: #f0f2f6;
        }
        .user-msg {
            background-color: #d1e7dd;
            color: #000;
        }
        .assistant-msg {
            background-color: #fff3cd;
            color: #000;
        }
        .sidebar .css-1d391kg {
            background-color: #f5f5f5;
        }
        .css-10trblm {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Agentic AI System</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Smart Query Handler</h4>", unsafe_allow_html=True)
st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("Controls")
    st.write("Manage your chat history or actions.")

    if st.button("Clear Chat"):
        st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg["role"] == "user":
            st.markdown(f": {msg['content']}", unsafe_allow_html=True)
        else:
            st.markdown(f": {msg['content']}", unsafe_allow_html=True)

user_input = st.chat_input("Type your query...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("🤔 Let me think..."):
            try:
                intent = classify_intent(user_input)
                st.markdown(f"🧠 Detected Intent: `{intent}`", unsafe_allow_html=True)

                if intent == "ticket":
                    response = agent.run(user_input)
                elif intent == "info":
                    ai_response = llm.invoke(user_input)
                    response = ai_response.content
                else:
                    response = "⚠️ Sorry, I couldn't understand your request. Try rephrasing it."
            except Exception as e:
                response = f"❌ An error occurred: {e}"

            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
