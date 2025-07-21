import httpx
from telegram import Update
from telegram.ext import ContextTypes

async def ip_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠️ Использование: `/ip <ip_адрес>`")
        return
    ip = context.args[0]
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"https://ipinfo.io/{ip}/json")
        if resp.status_code == 200:
            data = resp.json()
            info = "\n".join(f"{k}: {v}" for k, v in data.items())
            await update.message.reply_text(f"📍 Информация об IP {ip}:\n{info}")
        else:
            await update.message.reply_text("❌ Не удалось получить информацию.")
    except Exception as e:
        await update.message.reply_text(f"🚫 Ошибка: {e}")
