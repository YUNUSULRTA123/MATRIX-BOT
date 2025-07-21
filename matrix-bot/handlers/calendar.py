import json
import os
from datetime import datetime
from telegram import Update
from telegram.ext import ContextTypes

EVENTS_FILE = "data/events.json"

# Убедимся, что файл существует
os.makedirs("data", exist_ok=True)
if not os.path.exists(EVENTS_FILE):
    with open(EVENTS_FILE, "w", encoding="utf-8") as f:
        json.dump([], f)

# Добавить событие
async def addevent_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        if len(args) < 3:
            await update.message.reply_text(
    "❗ Формат команды:\n"
    "/addevent <дата> <время> <описание>\n\n"
    "🧠 Пример:\n"
    "/addevent 20.07.2025 14:00 Встреча с дизайнером"
)

            return

        date_str = args[0]
        time_str = args[1]
        description = " ".join(args[2:])

        # Проверка формата даты и времени
        dt_str = f"{date_str} {time_str}"
        dt = datetime.strptime(dt_str, "%d.%m.%Y %H:%M")

        event = {
            "timestamp": dt.timestamp(),
            "date": date_str,
            "time": time_str,
            "description": description
        }

        with open(EVENTS_FILE, "r+", encoding="utf-8") as f:
            events = json.load(f)
            events.append(event)
            f.seek(0)
            json.dump(events, f, indent=2, ensure_ascii=False)
            f.truncate()

        await update.message.reply_text(f"Событие добавлено: {description} ({date_str} в {time_str})")

    except ValueError:
        await update.message.reply_text("Неверный формат. Используй: /addevent 16.07.2025 14:30 Собрание")

# Показать список событий
async def events_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        with open(EVENTS_FILE, "r", encoding="utf-8") as f:
            events = json.load(f)

        if not events:
            await update.message.reply_text("У тебя пока нет событий.")
            return

        # Сортировка по времени
        events.sort(key=lambda x: x["timestamp"])
        now = datetime.now().timestamp()

        message = "📅 Твои события:\n"
        for e in events:
            # Показывать только будущие события
            if e["timestamp"] >= now:
                message += f"• {e['date']} в {e['time']} — {e['description']}\n"

        await update.message.reply_text(message if message.strip() else "Нет предстоящих событий.")

    except Exception as e:
        await update.message.reply_text(f"Ошибка при чтении событий: {e}")
