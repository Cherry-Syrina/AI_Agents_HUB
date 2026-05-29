from groq import Groq
from youtube_transcript_api import YouTubeTranscriptApi
import re
from dotenv import load_dotenv

load_dotenv()

def get_video_id(url):
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11})',
        r'youtu\.be\/([0-9A-Za-z_-]{11})'
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def get_transcript(video_id):
    try:
        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(video_id)
        # Naye version mein .text attribute hota hai
        text = " ".join([snippet.text for snippet in transcript])
        return text[:8000]
    except Exception as e:
        return f"ERROR: {str(e)}"

def analyze_video(url):
    client = Groq()
    video_id = get_video_id(url)
    if not video_id:
        return "❌ Invalid YouTube URL."

    transcript = get_transcript(video_id)

    if transcript.startswith("ERROR"):
        return f"""❌ **Transcript fetch nahi ho saka**

**Reason:** {transcript}

**Ye videos try karo (English + transcript enabled):**
- `https://www.youtube.com/watch?v=rfscVS0vtbw`
- `https://www.youtube.com/watch?v=_uQrJ0TkZlc`
"""

    prompt = f"""Analyze this YouTube video transcript and give a detailed report:

1. 📋 **Video Overview** - Topic, type, what it covers
2. ⏱️ **Timestamps** - Key moments [MM:SS - MM:SS: summary]
3. 🔑 **Key Learning Points** - Main takeaways
4. 📚 **Content Organization** - Sections and themes

Transcript:
{transcript}

Respond in detailed markdown with emojis."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000
    )
    return response.choices[0].message.content