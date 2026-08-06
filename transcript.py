"""
YouTube transcript and metadata fetching.
Video-ID extraction and title lookup adapted from the original workshop script.
"""

import re
import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi

_ID_PATTERNS = [
    r"v=([^&]+)",
    r"youtu\.be/([^?]+)",
    r"embed/([^?]+)",
]


def extract_video_id(url: str) -> str:
    for pattern in _ID_PATTERNS:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    raise ValueError("Invalid YouTube URL: could not extract video ID.")


def get_video_title(url: str) -> str:
    try:
        ydl_opts = {"quiet": True, "skip_download": True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info.get("title", "Unknown Title")
    except Exception:
        return "Unknown Title"


def get_transcript(video_id: str) -> str:
    try:
        segments = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as e:
        raise ValueError(f"Transcript unavailable for this video: {e}")

    return " ".join(item["text"] for item in segments)


def fetch_video_data(url: str) -> dict:
    """
    Convenience wrapper: extract ID, fetch title and transcript together.
    Returns {"video_id", "title", "transcript"}.
    """
    video_id = extract_video_id(url)
    title = get_video_title(url)
    transcript = get_transcript(video_id)
    return {"video_id": video_id, "title": title, "transcript": transcript}
