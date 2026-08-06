"""
Prompt templates.

Kept separate from LLM-calling code so the prompt can be reused,
versioned, or swapped independently of how it's invoked.
"""

SUMMARY_PROMPT_TEMPLATE = """You are an expert technical educator.

Summarize the following YouTube transcript{title_clause}.

Provide:
1. Summary (150-200 words)
2. Five key points
3. Three important takeaways
4. Important keywords
5. Target audience
6. Difficulty level
7. Suggested next learning steps

Write in simple, clear English.
Format the response using headings and bullet points.

Transcript:
\"\"\"
{transcript}
\"\"\"
"""


def build_summary_prompt(transcript: str, title: str | None = None) -> str:
    """
    Build the summarization prompt for a given transcript.

    Args:
        transcript: Raw transcript text.
        title: Optional video title, included in the prompt for context.

    Returns:
        A fully formatted prompt string ready to send to the LLM.
    """
    if not transcript or not transcript.strip():
        raise ValueError("Transcript is empty; cannot build prompt.")

    title_clause = f' titled "{title}"' if title else ""

    return SUMMARY_PROMPT_TEMPLATE.format(
        title_clause=title_clause,
        transcript=transcript.strip(),
    )
