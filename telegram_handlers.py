from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ConversationHandler, CommandHandler, CallbackQueryHandler, MessageHandler, filters

# States
MUSIC, VIDEOS, STYLE, RESOLUTION, FPS, BITRATE, CONFIRM = range(7)

async def create(update: Update, context):
    context.user_data.clear()
    context.user_data['step'] = MUSIC
    await update.message.reply_text("Send me the music file (MP3).")

async def handle_audio(update: Update, context):
    if context.user_data.get('step') != MUSIC:
        return
    file = await update.message.audio.get_file()
    path = DOWNLOAD_DIR / f"{update.effective_user.id}_music.mp3"
    await file.download_to_drive(path)
    context.user_data['music'] = str(path)
    context.user_data['step'] = VIDEOS
    context.user_data['videos'] = []
    await update.message.reply_text("Music saved. Now send video files (one by one). Use /done when finished.")

# ... all conversation handlers and callbacks
