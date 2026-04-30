"""
YouTube Transcript Collection Script
------------------------------------
- Fetches transcripts for multiple YouTube videos
- Handles errors safely (missing transcripts, network issues)
- Saves output in structured markdown files
"""

from youtube_transcript_api import YouTubeTranscriptApi
import os
import time

# ==============================
# CONFIGURATION
# ==============================

video_ids = [
    "Add_video_id",       # Add original video_ids here
    "Add_video_id"
]

output_dir = "research/youtube-transcripts"
os.makedirs(output_dir, exist_ok=True)


# ==============================
# CORE FUNCTION
# ==============================

def fetch_transcript(video_id):
    try:
        print(f"\n🔄 Processing: {video_id}")

        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        if not transcript:
            print(f"⚠️ Empty transcript: {video_id}")
            return

        file_path = os.path.join(output_dir, f"{video_id}.md")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write("# YouTube Transcript\n\n")
            f.write(f"Video ID: {video_id}\n")
            f.write(f"Link: https://youtu.be/{video_id}\n\n")
            f.write("## Transcript\n\n")

            for line in transcript:
                f.write(line["text"] + "\n")

        print(f"✅ Saved: {file_path}")

    except Exception as e:
        print(f"❌ Failed: {video_id} → {str(e)}")


# ==============================
# EXECUTION LOOP
# ==============================

for vid in video_ids:
    fetch_transcript(vid)
    time.sleep(2)  # prevents rate limiting

print("\n🎉 All transcripts processed!")