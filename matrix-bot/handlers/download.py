import os
import asyncio
from yt_dlp import YoutubeDL
from telegram import Update
from telegram.ext import ContextTypes

async def download_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠️ Укажи ссылку на видео. Пример:\n/download https://youtu.be/jNQXAC9IVRw")
        return

    url = context.args[0]
    try:
        # Настройки yt-dlp
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': 'video.%(ext)s',
            'noplaylist': True,
            'quiet': True,
            'no_warnings': True,
            'cookiefile': 'cookies.txt',  # если понадобится авторизация
        }

        # Скачиваем видео
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)

        # Отправляем видео
        await update.message.reply_video(video=open(file_path, 'rb'), caption=f"📥 {info.get('title')}")
        os.remove(file_path)

    except Exception as e:
        await update.message.reply_text(f"🚫 Ошибка: {e}")
