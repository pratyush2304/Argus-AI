import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    print("\n[Warning] GROQ_API_KEY is not set in your .env file.")
    print("Please set your API key in .env before initiating chat calls.\n")

DEFAULT_MODEL = "openai/gpt-oss-120b"

SYSTEM_INSTRUCTION = (
    "You are a helpful, clear, and intelligent AI assistant. "
    "Provide concise and structured answers whenever possible."
)
