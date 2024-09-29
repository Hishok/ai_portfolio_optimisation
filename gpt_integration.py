from transformers import pipeline

# Initialize the Hugging Face model pipeline
model = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B", pad_token_id=50256)

def interpret_preferences(input_text):
    """
    Uses Hugging Face GPT model to interpret the user's investment preferences.
    """
    prompt = f"Summarize the following investment preferences in clear and concise language: {input_text}. Focus on low-risk, value, growth, and diversification in that order."
    response = model(prompt, max_length=100, num_return_sequences=1, truncation=True, clean_up_tokenization_spaces=False)
    return response[0]['generated_text'].strip()

def suggest_funds(preferences):
    """
    Uses Hugging Face GPT model to suggest appropriate ETFs based on the user's preferences.
    """
    prompt = f"Suggest 3-5 well-known ETFs for the following investment preferences: {preferences}. Provide simple recommendations with low fees and high diversification."
    response = model(prompt, max_length=100, num_return_sequences=1, truncation=True, clean_up_tokenization_spaces=False)
    return response[0]['generated_text'].strip()

def explain_portfolio(weights, selected_etfs):
    """
    Uses Hugging Face GPT model to explain the portfolio decisions.
    """
    prompt = f"Explain the portfolio based on these ETFs: {selected_etfs} and the following weights: {weights}. Focus on diversification, risk, and expected return, providing a clear and concise explanation."
    response = model(prompt, max_length=200, num_return_sequences=1, truncation=True, clean_up_tokenization_spaces=False)
    return response[0]['generated_text'].strip()
