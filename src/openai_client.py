import os

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()


def get_client():
    """Get an authenticated OpenAI client.

    Returns:
        OpenAI: An authenticated OpenAI client instance

    """
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
