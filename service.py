"""
Service layer: ties transcript fetching, prompt building, and the LLM
call together. This is the single function both the API and any future
caller (CLI, worker, etc.) should use.
"""

from transcript import fetch_video_data
from prompts import build_summary_prompt
from llm import summarize as llm_summarize


def summarize_youtube_video(url: str) -> dict:
    data = fetch_video_data(url)

    prompt = build_summary_prompt(
        transcript=data["transcript"],
        title=data["title"],
    )

    summary = llm_summarize(prompt)

    return {
        "video_id": data["video_id"],
        "title": data["title"],
        "summary": summary,
    }
