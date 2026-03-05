import cv2
import numpy as np

def detect_scenes(video_path: str, threshold: float = 30.0) -> list:
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    clips = []
    prev_frame = None
    scene_start = 0.0
    for frame_idx in range(0, total_frames, int(fps)):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if prev_frame is not None:
            diff = cv2.absdiff(gray, prev_frame)
            mean_diff = np.mean(diff)
            if mean_diff > threshold:
                if frame_idx/fps - scene_start > 1.0:
                    clips.append({
                        "path": video_path,
                        "start": scene_start,
                        "end": frame_idx/fps,
                        "duration": frame_idx/fps - scene_start,
                        "type": "action" if mean_diff > 50 else "normal",
                        "brightness": np.mean(gray)
                    })
                scene_start = frame_idx/fps
        prev_frame = gray
    cap.release()
    return clips
