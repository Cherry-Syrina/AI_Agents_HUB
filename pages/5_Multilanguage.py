import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Multi-Language Team", page_icon="👥", layout="wide")

st.title("👥 Multi-Language Team")
st.markdown("**One question — answers in English, Hindi and Chinese**")
st.markdown("---")

client = Groq()

st.markdown("**Example questions:**")
st.code("What is Artificial Intelligence?\nWhat is the capital of India?\nHow does the internet work?")

query = st.text_input("Enter your question:", placeholder="What is Artificial Intelligence?")

if st.button("🌐 Get All Responses", use_container_width=True):
    if query:
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("🇬🇧 English")
            with st.spinner("Thinking..."):
                r = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant. Answer ONLY in English."},
                        {"role": "user", "content": query}
                    ],
                    max_tokens=500
                )
                st.markdown(r.choices[0].message.content)

        with col2:
            st.subheader("🇮🇳 Hindi")
            with st.spinner("Thinking..."):
                r = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant. Answer ONLY in Hindi language."},
                        {"role": "user", "content": query}
                    ],
                    max_tokens=500
                )
                st.markdown(r.choices[0].message.content)

        with col3:
            st.subheader("🇨🇳 Chinese")
            with st.spinner("Thinking..."):
                r = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant. Answer ONLY in Chinese language."},
                        {"role": "user", "content": query}
                    ],
                    max_tokens=500
                )
                st.markdown(r.choices[0].message.content)

    else:
        st.warning("⚠️ Please enter a question first.")