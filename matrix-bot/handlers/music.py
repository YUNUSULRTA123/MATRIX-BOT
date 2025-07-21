from telegram import Update
from telegram.ext import ContextTypes
import random

songs = [
    "🎵 Queen - Bohemian Rhapsody",
    "🎵 The Beatles - Let It Be",
    "🎵 Radiohead - Creep",
    "🎵 Nirvana - Smells Like Teen Spirit",
    "🎵 Daft Punk - Get Lucky",
    "🎵 Steve Lacy - Bad Habit",
]

async def music_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    song = random.choice(songs)
    await update.message.reply_text(f"Музыкальная рекомендация: {song}")
