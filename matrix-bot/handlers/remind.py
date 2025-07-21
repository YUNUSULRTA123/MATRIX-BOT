import asyncio
import re

async def remind_handler(update, context):
    if not context.args:
        await update.message.reply_text(
            "❗ Ты забыл указать время и сообщение.\n\n"
            "Формат: /remind <время> <сообщение>\n"
            "Пример: /remind 10m Выпить воды"
        )
        return

    if len(context.args) < 2:
        await update.message.reply_text(
            "❗ Укажи и время, и сообщение.\n"
            "Пример: /remind 5m Проверить чайник"
        )
        return

    time_str = context.args[0]
    message = " ".join(context.args[1:])

    match = re.match(r"^(\d+)([smh])$", time_str)
    if not match:
        await update.message.reply_text(
            "❗ Некорректный формат времени.\n"
            "Поддерживаются секунды (s), минуты (m), часы (h).\n"
            "Пример: 10s, 5m, 2h"
        )
        return

    amount, unit = int(match.group(1)), match.group(2)
    seconds = {"s": 1, "m": 60, "h": 3600}[unit]
    delay = amount * seconds

    await update.message.reply_text(f"⏳ Напомню через {amount}{unit}: {message}")
    await asyncio.sleep(delay)
    await update.message.reply_text(f"⏰ Напоминание: {message}")
