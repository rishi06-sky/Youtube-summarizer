"""
Configuration and settings.
Loads the Groq API key from a .env file (never hardcode keys in source).
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    GROQ_MODEL: str = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
    TEMPERATURE: float = float(os.getenv("SUMMARY_TEMPERATURE", "0.3"))

    def validate(self):
        if not self.GROQ_API_KEY:
            raise RuntimeError(
                "GROQ_API_KEY is not set. Create a .env file "
                "(see .env.example) with your Groq API key."
            )


settings = Settings()
