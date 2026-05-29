import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Memory Agent", page_icon="🧠", layout="centered")

st.title("🧠 Memory Agent")
st.markdown("**This agent remembers your conversation history**")
st.markdown("---")

if "memory_messages" not in st.session_state:
    st.session_state.memory_messages = []

client = Groq()

for msg in st.session_state.memory_messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Tell me something or ask anything..."):
    st.session_state.memory_messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful, friendly assistant with memory. Remember everything the user tells you. Answer naturally and conversationally."
                    }
                ] + st.session_state.memory_messages,
                max_tokens=1000
            )
            reply = response.choices[0].message.content
        st.markdown(reply)

    st.session_state.memory_messages.append({"role": "assistant", "content": reply})

if st.button("🗑️ Clear Chat"):
    st.session_state.memory_messages = []
    st.rerun()