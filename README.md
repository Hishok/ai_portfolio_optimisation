# AI-Powered Portfolio Optimisation Dashboard

This project is a **work in progress** for building an AI-powered portfolio optimisation dashboard using **Streamlit**, **Hugging Face's GPT-Neo model**, and other Python libraries like **yfinance**. The goal of this project is to create a tool that allows users to optimise their investment portfolios by suggesting funds based on preferences, performing financial analysis, and displaying relevant news.

---

## Project Overview

The dashboard is designed to perform the following key tasks:

1. **User Input**: The user provides their portfolio preferences, such as low-risk or diversified investments.
2. **AI-Powered Suggestions**: The AI model suggests ETFs (Exchange Traded Funds) based on these preferences.
3. **Portfolio Optimisation**: The selected ETFs are optimised using mean-variance optimisation to create an efficient portfolio.
4. **Financial Performance**: Daily and monthly performance data is displayed with interactive charts, showing the portfolio's returns.
5. **Relevant News Articles**: The dashboard fetches relevant financial news articles related to the selected ETFs.

### Work in Progress

While significant progress has been made, this project is still under development. There are still several errors and areas that need improvement:

- **Model Errors**: The Hugging Face GPT-Neo model has been integrated to generate natural language outputs (e.g., fund suggestions and portfolio explanations), but the generated text can sometimes be unclear or not directly relevant. Work is ongoing to fine-tune the prompts to get better results.
  
- **OpenAI Integration Issue**: Initially, I attempted to use OpenAI's models for text generation (such as GPT-3 or GPT-4). However, due to the cost associated with using OpenAI's paid API, I had to switch to Hugging Face's open-source models. The current model (GPT-Neo) is less costly but also less powerful than OpenAI's models.

- **Optimisation Bugs**: The portfolio optimisation logic is functional, but there are some edge cases that result in incorrect weights or performance data. Further work is needed to ensure consistent and accurate results.

- **News Fetching Issues**: The integration with the News API is not always reliable, and sometimes no articles are returned for relevant funds. This is an ongoing issue that needs to be addressed.

---

## How to Run the Project

To run this project locally, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Hishok/ai_portfolio_optimisation.git

2. Navigate into the project directory:

   ```bash
   cd ai_portfolio_optimisation

3. Create and activate a Python virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate


4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

5. Run the Streamlit app:

   ```bash
  streamlit run app.py

## Future Improvements: 
- Better Model Integration: Explore other models on Hugging Face or potentially switch back to OpenAI if a more cost-effective option becomes available.
- Error Handling: Improve error handling across the entire project to catch and display meaningful messages for users.
- Portfolio Performance Improvements: Refine the portfolio optimisation and performance calculations to ensure accuracy.
- UI/UX Enhancements: Make the dashboard more visually appealing and improve interactivity with the graphs and other UI elements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

### Steps to Add or Fix the README:

1. **Edit the `README.md`** in your project directory:
   - Open your project directory.
   - Open the `README.md` file or create it if it doesn’t exist.
   - Paste the updated content above.

2. **Commit and Push to GitHub**:

   ```bash
   git add README.md
   git commit -m "Update README.md with License section"
   git push origin master
