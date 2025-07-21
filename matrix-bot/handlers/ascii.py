import pyfiglet
from telegram import Update
from telegram.ext import ContextTypes

async def ascii_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args) or "Hello"
    try:
        art = pyfiglet.figlet_format(text)
        await update.message.reply_text(f"```\n{art}\n```", parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"🚫 Ошибка: {e}")
