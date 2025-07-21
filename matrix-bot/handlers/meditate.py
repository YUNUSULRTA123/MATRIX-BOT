import asyncio
from telegram import Update
from telegram.ext import ContextTypes

async def meditate_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    try:
        await context.bot.send_chat_action(chat_id, "typing")
        await asyncio.sleep(1)
        await context.bot.send_message(chat_id, "🧘 Давай немного помедитируем. Закрой глаза и сделай глубокий вдох...")

        await asyncio.sleep(4)
        await context.bot.send_message(chat_id, "😌 Представь, как с каждым выдохом уходит напряжение...")

        await asyncio.sleep(6)
        await context.bot.send_message(chat_id, "🌿 Просто будь здесь и сейчас...")

        await asyncio.sleep(6)
        await context.bot.send_message(chat_id, "✨ Хорошо. Потихоньку возвращайся в реальность.")

        await asyncio.sleep(3)
        await context.bot.send_message(chat_id, "Молодец 🙏 Ты сделал(а) шаг к спокойствию.")

    except Exception as e:
        await context.bot.send_message(chat_id, f"🚫 Больше злись потому что я тоже устал 🤣🤣🤣🤣: {e}")
