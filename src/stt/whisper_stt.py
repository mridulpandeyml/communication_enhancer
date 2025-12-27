import whisper
import soundfile as sf
import numpy as np

model = whisper.load_model("base")

def transcribe_audio(audio_path):
    # Load audio
    audio, sample_rate = sf.read(audio_path)

    # 🔑 CRITICAL FIX: convert to float32
    audio = audio.astype(np.float32)

    # Optional: ensure mono
    if audio.ndim > 1:
        audio = np.mean(audio, axis=1)

    result = model.transcribe(audio, fp16=False)

    transcript = result["text"]
    segments = result["segments"]

    return transcript, segments
