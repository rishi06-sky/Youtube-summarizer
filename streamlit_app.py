"""
Streamlit UI for the YouTube Summarizer.
Talks to the FastAPI backend over HTTP — run the API first:
    uvicorn main:app --reload
"""

import streamlit as st
import requests

API_URL = "http://localhost:8000/summarize"

st.set_page_config(page_title="YouTube Summarizer", page_icon="📺", layout="centered")

st.title("📺 YouTube Summarizer")
st.caption("Paste a YouTube link, get an LLM-generated summary.")

url = st.text_input("YouTube URL", placeholder="https://www.youtube.com/watch?v=...")

col1, col2 = st.columns([1, 4])
with col1:
    run = st.button("Summarize", type="primary")

if run:
    if not url.strip():
        st.warning("Please enter a YouTube URL.")
    else:
        with st.spinner("Fetching transcript and generating summary..."):
            try:
                resp = requests.post(API_URL, json={"youtube_url": url}, timeout=90)
                resp.raise_for_status()
                data = resp.json()

                st.subheader(data["title"])
                st.divider()
                st.markdown(data["summary"])

            except requests.exceptions.HTTPError as e:
                try:
                    detail = e.response.json().get("detail", str(e))
                except Exception:
                    detail = str(e)
                st.error(f"Error: {detail}")

            except requests.exceptions.ConnectionError:
                st.error(
                    "Could not reach the API. Is it running? "
                    "Start it with: uvicorn main:app --reload"
                )

            except Exception as e:
                st.error(f"Something went wrong: {e}")
