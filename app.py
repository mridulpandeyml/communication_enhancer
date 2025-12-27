import streamlit as st
from src.input.audio_capture import record_audio
from src.stt.whisper_stt import transcribe_audio
from src.storage.session_logger import save_transcript

st.title("🎤 AI Interview & Communication Coach")
st.subheader("Phase 1: Audio to Transcript")

duration = st.slider("Recording duration (seconds)", 10, 60, 30)

if st.button("Start Recording"):
    audio_path, session_id = record_audio(duration)
    
    with st.spinner("Transcribing audio..."):
        transcript, segments = transcribe_audio(audio_path)

    save_path = save_transcript(session_id, transcript, segments)

    st.success("Transcript generated successfully!")

    st.markdown("### 📝 Transcript")
    st.write(transcript)

    st.markdown("### 💾 Saved At")
    st.code(save_path)
