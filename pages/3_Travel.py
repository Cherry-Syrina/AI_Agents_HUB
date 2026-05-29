import streamlit as st
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Travel Agent", page_icon="✈️", layout="centered")

st.title("✈️ Travel Agent")
st.markdown("**Travel recommendations, safety info and destination guides**")
st.markdown("---")

@st.cache_resource
def get_agent():
    return Agent(
        model=Groq(id="llama-3.3-70b-versatile"),
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions="You are a helpful and expert travel agent. Search for current information and give detailed travel advice.",
        add_datetime_to_context=True,
    )

agent = get_agent()

st.markdown("**Example queries:**")
st.code("Travel tips for Dubai\nBest time to visit Thailand\nIs it safe to travel to Japan right now?")

query = st.text_input("Enter your travel question:", placeholder="Travel tips for Dubai")

if st.button("✈️ Get Travel Advice", use_container_width=True):
    if query:
        with st.spinner("🌍 Searching for information..."):
            response = agent.run(query)
        st.success("✅ Done!")
        st.markdown("---")
        st.markdown(response.content)
    else:
        st.warning("⚠️ Please enter a question first.")