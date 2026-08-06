# YouTube Summarizer

Fetches a YouTube video's transcript and title, then generates a structured
summary (summary, key points, takeaways, keywords, audience, difficulty,
next steps) using an LLM via Groq.

## Structure

```
youtube-summarizer/
├── app/
│   ├── main.py         # FastAPI app + /summarize endpoint
│   ├── config.py        # Settings (API key, model, temperature)
│   ├── prompts.py        # Reusable prompt template
│   ├── transcript.py     # Video ID extraction, title + transcript fetch
│   ├── llm.py             # Groq client wrapper
│   ├── service.py         # Orchestrates transcript -> prompt -> LLM
│   └── schemas.py         # Request/response models
├── ui/
│   └── streamlit_app.py   # Streamlit front-end
├── requirements.txt
└── .env.example
```

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file (copy `.env.example`) and add your Groq API key:
   ```bash
   cp .env.example .env
   ```

3. Start the API:
   ```bash
   uvicorn app.main:app --reload
   ```
   Swagger docs at http://localhost:8000/docs

4. In a second terminal, start the UI:
   ```bash
   streamlit run ui/streamlit_app.py
   ```

## API

`POST /summarize`

Request:
```json
{ "youtube_url": "https://www.youtube.com/watch?v=VIDEO_ID" }
```

Response:
```json
{
  "video_id": "VIDEO_ID",
  "title": "Video Title",
  "summary": "## Summary\n..."
}
```

## Notes / next steps

- Transcripts fail for videos with disabled captions or non-English audio —
  currently surfaced as a 400 error with the underlying reason.
- Long transcripts may exceed model context; consider chunking + a
  summary-of-summaries pass for very long videos.
- Add caching (e.g. keyed on video_id) to avoid re-summarizing the same video.
- Swap `llm.py` for a different provider (e.g. Anthropic) without touching
  prompts.py, service.py, or main.py.
