import httpx
from telegram import Update
from telegram.ext import ContextTypes

async def shorten_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠️ Введите ссылку после команды. Пример:\n/shorten https://example.com")
        return

    original_url = context.args[0]
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"https://is.gd/create.php?format=simple&url={original_url}")
        if response.status_code == 200:
            short_link = response.text
            await update.message.reply_text(f"🔗 Сокращённая ссылка:\n{short_link}")
        else:
            await update.message.reply_text("❌ Не удалось сократить ссылку.")
    except Exception as e:
        await update.message.reply_text(f"🚫 Ошибка: {e}")
