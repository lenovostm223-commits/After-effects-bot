import os
from pathlib import Path

BOT_TOKEN = os.environ["BOT_TOKEN"]
ADMIN_IDS = [int(id) for id in os.environ.get("ADMIN_IDS", "").split(",") if id]

BASE_DIR = Path("/home/runner/workspace")
DOWNLOAD_DIR = BASE_DIR / "downloads"
OUTPUT_DIR = BASE_DIR / "outputs"
LOG_DIR = BASE_DIR / "logs"
DOWNLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

MAX_CONCURRENT_JOBS = 2  # Replit's free tier can handle 2-3 concurrent jobs
MAX_FILE_SIZE_MB = 50    # Telegram bot limit
ALLOWED_VIDEO_EXT = ('.mp4', '.mkv', '.mov')
ALLOWED_AUDIO_EXT = ('.mp3', '.m4a', '.aac')
