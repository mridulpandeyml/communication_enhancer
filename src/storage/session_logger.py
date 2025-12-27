import json
import os
from datetime import datetime

def save_transcript(session_id, transcript, segments, save_dir="data/processed/transcripts"):
    os.makedirs(save_dir, exist_ok=True)

    session_data = {
        "session_id": session_id,
        "timestamp": datetime.now().isoformat(),
        "transcript": transcript,
        "segments": segments
    }

    file_path = os.path.join(save_dir, f"{session_id}.json")

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(session_data, f, indent=4)

    return file_path
