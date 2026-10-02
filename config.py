import os
from dotenv import load_dotenv

load_dotenv(override=True)


def _get_key() -> str:
    key = os.getenv("GROQ_API_KEY")
    if not key:
        try:
            import streamlit as st
            key = st.secrets.get("GROQ_API_KEY")
        except Exception:
            key = None
    return (key or "").strip().strip("\"'")


GROQ_API_KEY = _get_key()

if not GROQ_API_KEY:
    print("\n[Warning] GROQ_API_KEY is not set (.env locally, or Secrets on Streamlit Cloud).\n")

DEFAULT_MODEL = "openai/gpt-oss-120b"

SYSTEM_INSTRUCTION = (
    "You are a helpful, clear, and intelligent AI assistant. "
    "Provide concise and structured answers whenever possible."
)