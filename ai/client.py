from core.config import Config
from langchain_openai import ChatOpenAI

def get_openai_client():
    api_key = Config.OPENAI_API_KEY
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable is required. "
            "Please set it in your .env file or environment variables."
        )
    return ChatOpenAI(api_key=api_key, model="gpt-4o")
