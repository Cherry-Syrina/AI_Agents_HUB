import streamlit as st
from groq import Groq
import requests
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Finance Agent", page_icon="📈", layout="centered")

st.title("📈 Finance Agent")
st.markdown("**Real-time stock prices, analysis and market insights**")
st.markdown("---")

client = Groq()
AV_KEY = os.getenv("ALPHA_VANTAGE_KEY")

def get_stock_price(symbol):
    try:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={AV_KEY}"
        r = requests.get(url, timeout=10)
        data = r.json()
        quote = data.get("Global Quote", {})
        if not quote or not quote.get("05. price"):
            return None
        return {
            "symbol": quote.get("01. symbol"),
            "price": float(quote.get("05. price", 0)),
            "change": quote.get("09. change"),
            "change_pct": quote.get("10. change percent"),
            "high": quote.get("03. high"),
            "low": quote.get("04. low"),
            "volume": quote.get("06. volume"),
            "prev_close": quote.get("08. previous close"),
        }
    except:
        return None

def get_company_overview(symbol):
    try:
        url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={AV_KEY}"
        r = requests.get(url, timeout=10)
        data = r.json()
        if not data.get("Symbol"):
            return None
        return {
            "name": data.get("Name"),
            "sector": data.get("Sector"),
            "pe_ratio": data.get("PERatio"),
            "market_cap": data.get("MarketCapitalization"),
            "52_week_high": data.get("52WeekHigh"),
            "52_week_low": data.get("52WeekLow"),
            "analyst_target": data.get("AnalystTargetPrice"),
            "dividend_yield": data.get("DividendYield"),
            "description": data.get("Description", "")[:300],
        }
    except:
        return None

# Common ticker mapping
TICKERS = {
    "apple": "AAPL", "aapl": "AAPL",
    "microsoft": "MSFT", "msft": "MSFT",
    "google": "GOOGL", "googl": "GOOGL", "alphabet": "GOOGL",
    "tesla": "TSLA", "tsla": "TSLA",
    "amazon": "AMZN", "amzn": "AMZN",
    "meta": "META", "facebook": "META",
    "nvidia": "NVDA", "nvda": "NVDA",
    "netflix": "NFLX", "nflx": "NFLX",
    "tcs": "TCS.BSE", "reliance": "RELIANCE.BSE",
    "infosys": "INFY", "wipro": "WIPRO.BSE",
    "hdfc": "HDB", "icici": "IBN",
    "nifty": "NIFTY50.NSE", "sensex": "SENSEX.BSE",
}

st.markdown("**Example queries:**")
st.code("Analyze AAPL stock\nCompare MSFT vs GOOGL\nShould I invest in Tesla?\nNifty 50 analysis")

query = st.text_input("Enter your finance question:", placeholder="Analyze AAPL stock")

if st.button("🔍 Analyze", use_container_width=True):
    if query:
        with st.spinner("📊 Fetching real-time market data..."):
            query_lower = query.lower()
            stock_info = ""
            found_tickers = []

            for keyword, ticker in TICKERS.items():
                if keyword in query_lower:
                    if ticker not in found_tickers:
                        found_tickers.append(ticker)
                        price_data = get_stock_price(ticker)
                        overview = get_company_overview(ticker)

                        if price_data:
                            stock_info += f"""
## {ticker}
**Current Price:** ${price_data['price']}
**Change:** {price_data['change']} ({price_data['change_pct']})
**High:** ${price_data['high']} | **Low:** ${price_data['low']}
**Prev Close:** ${price_data['prev_close']}
**Volume:** {price_data['volume']}
"""
                        if overview:
                            stock_info += f"""
**Company:** {overview['name']}
**Sector:** {overview['sector']}
**P/E Ratio:** {overview['pe_ratio']}
**Market Cap:** ${overview['market_cap']}
**52W High:** ${overview['52_week_high']} | **52W Low:** ${overview['52_week_low']}
**Analyst Target:** ${overview['analyst_target']}
**About:** {overview['description']}
"""

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert investment analyst. Use the real-time data provided to give detailed, accurate analysis. Use markdown with tables. Be specific with numbers from the data."
                    },
                    {
                        "role": "user",
                        "content": f"Question: {query}\n\nReal-time Stock Data:\n{stock_info if stock_info else 'No specific stock detected. Answer based on financial knowledge.'}"
                    }
                ],
                max_tokens=1500
            )

        st.success("✅ Done!")
        st.markdown("---")

        # Real-time data table dikhao
        if found_tickers:
            st.subheader("📊 Live Data")
            for ticker in found_tickers:
                price_data = get_stock_price(ticker)
                if price_data:
                    col1, col2, col3, col4 = st.columns(4)
                    col1.metric("Price", f"${price_data['price']:.2f}")
                    col2.metric("Change", price_data['change'], price_data['change_pct'])
                    col3.metric("High", f"${price_data['high']}")
                    col4.metric("Low", f"${price_data['low']}")
            st.markdown("---")

        st.markdown(response.choices[0].message.content)

    else:
        st.warning("⚠️ Please enter a question first.")
