from fastapi import FastAPI, HTTPException
from app.schemas import SummarizeRequest, SummarizeResponse
from app.service import summarize_youtube_video

app = FastAPI(
    title="YouTube Summarizer API",
    description="Fetches a YouTube transcript and returns an LLM-generated summary.",
    version="1.0.0",
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/summarize", response_model=SummarizeResponse)
def summarize_endpoint(req: SummarizeRequest):
    try:
        result = summarize_youtube_video(str(req.youtube_url))
        return SummarizeResponse(**result)
    except ValueError as e:
        # Bad URL, no transcript available, etc. -> client error
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        # Missing API key / config issue -> server misconfiguration
        raise HTTPException(status_code=500, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to summarize video.")
