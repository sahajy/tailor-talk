import streamlit as st
import requests

st.set_page_config(page_title="TailorTalk AI", layout="centered")

st.title("🧵 TailorTalk AI - Book Meetings with Ease")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.chat_input("Say something...")

if user_input:
    st.session_state.chat.append(("user", user_input))

    with st.spinner("Thinking..."):
        try:
            res = requests.post(
                "http://127.0.0.1:8000/chat",
                json={"message": user_input},
                timeout=30
            )
            ai_response = res.json()["response"]
        except Exception as e:
            ai_response = f"⚠️ An error occurred: {e}"

    st.session_state.chat.append(("ai", ai_response))

for role, msg in st.session_state.chat:
    with st.chat_message(role):
        st.markdown(msg)
