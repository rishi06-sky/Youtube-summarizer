from pydantic import BaseModel, HttpUrl


class SummarizeRequest(BaseModel):
    youtube_url: HttpUrl


class SummarizeResponse(BaseModel):
    video_id: str
    title: str
    summary: str
