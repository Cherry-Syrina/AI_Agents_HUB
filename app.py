import streamlit as st

st.set_page_config(
    page_title="AI Agents Hub",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>
    .agent-card {
        background: linear-gradient(135deg, #1e1e2e, #2a2a3e);
        border: 1px solid #3a3a5e;
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0;
        color: white;
    }
    .title-text {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #a78bfa, #60a5fa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title-text">🤖 AI Agents Hub</p>', unsafe_allow_html=True)
st.markdown("**Powered by Groq Free API + LLaMA 3.3 70B**")
st.markdown("---")

st.subheader("👈 Select an agent from the left sidebar")
st.markdown("")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="agent-card">
        <h3>🎥 YouTube Analyzer</h3>
        <p>Get detailed analysis, timestamps and key points of any YouTube video.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="agent-card">
        <h3>📈 Finance Agent</h3>
        <p>Get stock prices, analyst recommendations and market analysis.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="agent-card">
        <h3>✈️ Travel Agent</h3>
        <p>Get travel recommendations, safety info and destination guides.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="agent-card">
        <h3>🧠 Memory Agent</h3>
        <p>Chat with an AI that remembers your conversation history.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("")
st.markdown("""
<div class="agent-card">
    <h3>👥 Multi-Language Team</h3>
    <p>Ask one question — get answers in English, Hindi and Chinese</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.caption("Built with ❤️ by Sushma Shukla")
