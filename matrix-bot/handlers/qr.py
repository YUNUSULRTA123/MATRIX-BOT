import qrcode
from io import BytesIO
from telegram import Update
from telegram.ext import ContextTypes

async def qr_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = " ".join(context.args)
    if not data:
        await update.message.reply_text("⚠️ Использование: `/qr <текст или ссылка>`")
        return
    img = qrcode.make(data)
    bio = BytesIO()
    img.save(bio, format="PNG")
    bio.seek(0)
    await update.message.reply_photo(photo=bio)
