import sqlite3
import json
from models import User, Job, JobStatus, Style

class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT,
                    first_name TEXT,
                    join_date REAL,
                    jobs_count INTEGER DEFAULT 0,
                    banned INTEGER DEFAULT 0
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS jobs (
                    id TEXT PRIMARY KEY,
                    user_id INTEGER,
                    style TEXT,
                    music_file TEXT,
                    video_files TEXT,
                    output_name TEXT,
                    resolution TEXT,
                    fps INTEGER,
                    bitrate TEXT,
                    status TEXT,
                    progress INTEGER,
                    created_at REAL,
                    started_at REAL,
                    completed_at REAL,
                    error TEXT,
                    cancel_requested INTEGER
                )
            ''')
            conn.commit()
    # ... CRUD methods (get_user, add_job, update_job, etc.)
