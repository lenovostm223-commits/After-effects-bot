import asyncio
import threading
from telegram.ext import Application
from config import BOT_TOKEN
from flask_server import run_flask
from job_manager import JobManager
from database import db
import handlers

async def main():
    # Start job manager
    job_manager = JobManager(max_concurrent=2)
    asyncio.create_task(job_manager.start())

    # Telegram bot
    app = Application.builder().token(BOT_TOKEN).build()
    handlers.register_handlers(app)
    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    # Keep running
    await asyncio.Event().wait()

if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()
    asyncio.run(main())
