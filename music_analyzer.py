import librosa
import numpy as np

def analyze_music(path: str) -> dict:
    y, sr = librosa.load(path, sr=None, duration=300)  # limit to 5 minutes
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    beat_frames = librosa.frames_to_time(beats, sr=sr)
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    # Segment detection (optional)
    boundaries = librosa.segment.agglomerative(y, k=8)
    segments = []
    for i in range(len(boundaries)-1):
        segments.append({
            "start": librosa.frames_to_time(boundaries[i], sr=sr),
            "end": librosa.frames_to_time(boundaries[i+1], sr=sr)
        })
    return {
        "duration": librosa.get_duration(y=y, sr=sr),
        "bpm": tempo,
        "beats": beat_frames.tolist(),
        "onset_strength": onset_env.tolist(),
        "segments": segments
  }
