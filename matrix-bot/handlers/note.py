import os
import json
from telegram import Update
from telegram.ext import ContextTypes

NOTES_FILE = "data/notes.json"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return {}
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_notes(notes):
    os.makedirs("data", exist_ok=True)
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2)

async def note_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    args = context.args

    if not args:
        await update.message.reply_text("Команды:\n/note add <текст>\n/note list\n/note delete <номер>")
        return

    command = args[0].lower()
    notes = load_notes()

    if command == "add":
        note_text = " ".join(args[1:])
        if not note_text:
            await update.message.reply_text("❗ Укажи текст заметки.")
            return
        notes.setdefault(user_id, []).append(note_text)
        save_notes(notes)
        await update.message.reply_text("✅ Заметка добавлена.")

    elif command == "list":
        user_notes = notes.get(user_id, [])
        if not user_notes:
            await update.message.reply_text("📭 У тебя пока нет заметок.")
            return
        msg = "\n".join([f"{i+1}. {n}" for i, n in enumerate(user_notes)])
        await update.message.reply_text(f"📝 Твои заметки:\n{msg}")

    elif command == "delete":
        if len(args) < 2 or not args[1].isdigit():
            await update.message.reply_text("❗ Укажи номер заметки для удаления.")
            return
        index = int(args[1]) - 1
        user_notes = notes.get(user_id, [])
        if 0 <= index < len(user_notes):
            removed = user_notes.pop(index)
            save_notes(notes)
            await update.message.reply_text(f"🗑 Удалено: {removed}")
        else:
            await update.message.reply_text("❌ Неверный номер.")

    else:
        await update.message.reply_text("Неизвестная подкоманда. Используй: add / list / delete")
