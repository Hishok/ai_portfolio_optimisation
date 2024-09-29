import streamlit as st
from data_fetcher import fetch_etf_data, calculate_portfolio_performance, fetch_global_markets
from optimisation_methods import mean_variance_optimisation
from gpt_integration import interpret_preferences, explain_portfolio, suggest_funds
from fund_suggestions import etf_suggestions
from news_fetcher import fetch_news_articles
import pandas as pd

st.set_page_config(page_title="AI-Powered Portfolio Optimisation Dashboard", layout="wide")

# Title of the Dashboard
st.title("AI-Powered Portfolio Optimisation Dashboard")

# Global Market Overview
st.header("**Global Market Overview**")

with st.spinner("Fetching global market data..."):
    market_data = fetch_global_markets()

if market_data:
    col1, col2 = st.columns(2)
    for market, data in market_data.items():
        col1.metric(label=market, value=f"${data['last_price']:.2f}", 
                    delta=f"{data['change']:.2f} ({data['percent_change']:.2f}%)")
else:
    st.write("Unable to fetch global market data.")

# User Input for Portfolio Preferences
st.header("**Portfolio Optimisation**")
preferences = st.text_area("Describe your portfolio preferences (e.g., 'low-risk, diversified, focus on US equities')")

# Process the user's input with Hugging Face GPT
if st.button("Generate Portfolio"):
    if preferences:
        # Interpret Preferences
        st.subheader("**Interpreted Preferences**")
        try:
            st.write("Generating interpreted preferences...")
            interpreted_preferences = interpret_preferences(preferences)
            st.write(f"{interpreted_preferences}")
            st.write("Interpreted preferences successfully generated!")
        except Exception as e:
            st.error(f"Error interpreting preferences: {e}")
            st.stop()

        # Suggest Funds
        st.subheader("**Suggested ETFs**")
        try:
            st.write("Generating suggested funds...")
            suggested_funds = suggest_funds(preferences)
            st.write(f"{suggested_funds}")
            st.write("Suggested funds successfully generated!")
        except Exception as e:
            st.error(f"Error suggesting funds: {e}")
            st.stop()

        # Allow the user to select ETFs or use suggestions
        try:
            etfs = etf_suggestions()
            selected_etfs = st.multiselect("Select ETFs for your portfolio:", list(etfs.keys()), default=list(etfs.keys()))
            st.write(f"Selected ETFs: {selected_etfs}")
        except Exception as e:
            st.error(f"Error fetching ETF suggestions: {e}")
            st.stop()

        # Fetch ETF data starting from 1994
        try:
            st.write("Fetching ETF data...")
            returns, expected_returns, cov_matrix = fetch_etf_data(selected_etfs)
            st.write(f"Fetched data for ETFs: {selected_etfs}")
        except Exception as e:
            st.error(f"Error fetching ETF data: {e}")
            st.stop()

        # Optimise the portfolio using mean-variance optimisation
        try:
            st.write("Optimising portfolio...")
            optimal_weights = mean_variance_optimisation(expected_returns, cov_matrix)
            st.write(f"Optimal Weights: {optimal_weights}")
        except Exception as e:
            st.error(f"Error during portfolio optimisation: {e}")
            st.stop()

        # Display Optimised Portfolio Weights
        st.subheader("**Optimised Portfolio Weights**")
        try:
            # Convert weights to percentages
            weights_df = pd.DataFrame({
                'ETF': selected_etfs,
                'Weight (%)': [f"{weight * 100:.2f}%" for weight in optimal_weights]
            })
            st.bar_chart(weights_df.set_index('ETF'))
        except Exception as e:
            st.error(f"Error displaying portfolio weights: {e}")
            st.stop()

        # Show Daily and Monthly Portfolio Performance
        try:
            st.subheader("**Daily Performance (%)**")
            st.line_chart(daily_performance * 100)
            st.write("Daily performance of the portfolio in percentage. X-axis: Date, Y-axis: Daily Returns (%)")

            st.subheader("**Monthly Performance (%)**")
            st.line_chart(monthly_performance * 100)
            st.write("Monthly performance of the portfolio in percentage. X-axis: Date, Y-axis: Monthly Returns (%)")
        except Exception as e:
            st.error(f"Error calculating or displaying performance: {e}")
            st.stop()

        # Explain the Portfolio using Hugging Face GPT
        st.subheader("**Portfolio Explanation**")
        try:
            explanation = explain_portfolio(optimal_weights, selected_etfs)
            st.write(f"{explanation}")
        except Exception as e:
            st.error(f"Error explaining portfolio: {e}")
            st.stop()

        # Fetch Relevant News Articles for the Selected ETFs
        st.header("**Relevant News**")
        for etf in selected_etfs:
            st.subheader(f"**News for {etf}**:")
            try:
                news = fetch_news_articles(etf)
                if news:
                    for title, link in news:
                        st.markdown(f"- [{title}]({link})")
                else:
                    st.write("No relevant news articles found.")
            except Exception as e:
                st.error(f"Error fetching news for {etf}: {e}")

    else:
        st.warning("Please enter your portfolio preferences.")
