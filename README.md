# 🤖 AI Agents Hub

A multi-agent AI application built with **Groq's free API** (LLaMA 3.3 70B) and **Streamlit**. Five powerful AI agents in one app — all completely free!

## 🤖 Agents

| Agent | Description | Tools Used |
|-------|-------------|------------|
| 🎥 YouTube Analyzer | Video analysis, timestamps, key points | YouTube Transcript API + Groq |
| 📈 Finance Agent | Real-time stock prices & market analysis | Alpha Vantage API + Groq |
| ✈️ Travel Agent | Travel tips, safety info, destination guide | DuckDuckGo Search + Groq |
| 🧠 Memory Agent | Chat with conversation memory | Groq LLM |
| 👥 Multi-Language Team | One question in English, Hindi & Chinese | Groq LLM |

## 🛠️ Local Setup

### 1. Clone the Repository
git clone https://github.com/Cherry-Syrina/AI_Agents_HUB.git
cd AI_Agents_HUB

### 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Get Free API Keys
- Groq API Key: https://console.groq.com
- Alpha Vantage Key: https://www.alphavantage.co/support/#api-key

### 5. Setup .env file
GROQ_API_KEY=your_groq_key_here
ALPHA_VANTAGE_KEY=your_alpha_vantage_key_here

### 6. Run
streamlit run app.py

## ☁️ Streamlit Cloud Deploy

1. Go to https://share.streamlit.io
2. Connect this GitHub repo
3. Main file: app.py
4. Add secrets:
   GROQ_API_KEY = "your_key"
   ALPHA_VANTAGE_KEY = "your_key"

## 🔑 Environment Variables

| Variable | Required |
|----------|----------|
| GROQ_API_KEY | ✅ Yes |
| ALPHA_VANTAGE_KEY | ✅ Finance Agent |

## 🧰 Tech Stack
- Groq — Free LLM API
- Agno — AI Agent Framework  
- Streamlit — Web UI
- Alpha Vantage — Real-time Stock Data
- YouTube Transcript API — Video Transcripts
- DuckDuckGo Search — Web Search