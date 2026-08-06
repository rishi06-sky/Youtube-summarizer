"""
LLM client wrapper (Groq).
Kept isolated so the provider can be swapped without touching prompts or routes.
"""

from groq import Groq
from config import settings

_client: Groq | None = None


def get_client() -> Groq:
    global _client
    if _client is None:
        settings.validate()
        _client = Groq(api_key=settings.GROQ_API_KEY)
    return _client


def summarize(prompt: str) -> str:
    client = get_client()

    response = client.chat.completions.create(
        model=settings.GROQ_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=settings.TEMPERATURE,
    )

    content = response.choices[0].message.content
    if content is None:
        raise ValueError("LLM response missing content")
    return content
