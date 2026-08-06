"""
Configuration and settings.
Loads the Groq API key from a .env file (never hardcode keys in source).
"""

import os

try:
    from dotenv import load_dotenv
except ImportError as exc:
    raise ImportError(
        "python-dotenv is required to load .env settings. "
        "Install it with `pip install python-dotenv` or `pip install -r requirements.txt`."
    ) from exc

load_dotenv()


class Settings:
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "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")
    GROQ_MODEL: str = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
    TEMPERATURE: float = float(os.getenv("SUMMARY_TEMPERATURE", "0.3"))

    def validate(self):
        if not self.GROQ_API_KEY:
            raise RuntimeError(
                "GROQ_API_KEY is not set. Create a .env file "
                "(see .env) with your Groq API key."
            )


settings = Settings()
