from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch API keys from environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

