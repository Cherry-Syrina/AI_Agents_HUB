import streamlit as st
from groq import Groq
from duckduckgo_search import DDGS
import yfinance as yf
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Finance Agent", page_icon="📈", layout="centered")

st.title("📈 Finance Agent")
st.markdown("**Stock prices, analyst recommendations and market news**")
st.markdown("---")

client = Groq()

def web_search(query):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))
            return "\n".join([f"- {r['title']}: {r['body']}" for r in results])
    except Exception as e:
        return f"Search failed: {str(e)}"

def get_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        price = info.get('currentPrice') or info.get('regularMarketPrice')
        if not price:
            return None
        return f"""
Stock: {info.get('longName', ticker)}
Current Price: {price}
Previous Close: {info.get('previousClose', 'N/A')}
52 Week High: {info.get('fiftyTwoWeekHigh', 'N/A')}
52 Week Low: {info.get('fiftyTwoWeekLow', 'N/A')}
P/E Ratio: {info.get('trailingPE', 'N/A')}
Recommendation: {info.get('recommendationKey', 'N/A').upper()}
"""
    except:
        return None

common_tickers = {
    "apple": "AAPL", "aapl": "AAPL",
    "microsoft": "MSFT", "msft": "MSFT",
    "google": "GOOGL", "googl": "GOOGL",
    "tesla": "TSLA", "tsla": "TSLA",
    "amazon": "AMZN", "amzn": "AMZN",
    "meta": "META", "nvidia": "NVDA", "nvda": "NVDA",
    "reliance": "RELIANCE.NS", "tcs": "TCS.NS",
    "infosys": "INFY.NS", "wipro": "WIPRO.NS",
    "hdfc": "HDFCBANK.NS", "icici": "ICICIBANK.NS",
}

st.markdown("**Example queries:**")
st.code("Analyze AAPL stock\nNifty 50 current price\nShould I invest in Tesla?\nReliance stock analysis")

query = st.text_input("Enter your finance question:", placeholder="Nifty 50 current price")

if st.button("🔍 Analyze", use_container_width=True):
    if query:
        with st.spinner("📊 Fetching market data..."):
            query_lower = query.lower()
            stock_data = ""

            # yfinance se try karo
            for keyword, ticker in common_tickers.items():
                if keyword in query_lower:
                    data = get_stock_data(ticker)
                    if data:
                        stock_data += data + "\n"

            # Web search se latest data lo
            search_results = web_search(f"{query} stock price today 2025")

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert investment analyst. Use the provided data to give clear, accurate analysis. Use markdown with tables where helpful."
                    },
                    {
                        "role": "user",
                        "content": f"""Question: {query}

Stock Data (yfinance):
{stock_data if stock_data else 'Not available'}

Latest Web Search Results:
{search_results}

Give a detailed analysis based on above data."""
                    }
                ],
                max_tokens=1500
            )

        st.success("✅ Done!")
        st.markdown("---")
        st.markdown(response.choices[0].message.content)
    else:
        st.warning("⚠️ Please enter a question first.")