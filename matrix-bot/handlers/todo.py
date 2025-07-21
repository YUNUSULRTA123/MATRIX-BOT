import os
import json
from telegram import Update
from telegram.ext import ContextTypes

TODO_FILE = "data/todo.json"

def load_todos():
    if not os.path.exists(TODO_FILE):
        return {}
    with open(TODO_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_todos(todos):
    os.makedirs("data", exist_ok=True)
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, indent=2)

async def todo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    args = context.args

    if not args:
        await update.message.reply_text(
            "Команды:\n"
            "/todo add <задача>\n"
            "/todo list\n"
            "/todo done <номер>\n"
            "/todo delete <номер>"
        )
        return

    command = args[0].lower()
    todos = load_todos()
    user_todos = todos.setdefault(user_id, [])

    if command == "add":
        task = " ".join(args[1:])
        if not task:
            await update.message.reply_text("❗ Укажи задачу для добавления.")
            return
        user_todos.append({"task": task, "done": False})
        save_todos(todos)
        await update.message.reply_text(f"✅ Задача добавлена: {task}")

    elif command == "list":
        if not user_todos:
            await update.message.reply_text("📭 Список задач пуст.")
            return
        msg_lines = []
        for i, item in enumerate(user_todos, start=1):
            status = "✅" if item["done"] else "❌"
            msg_lines.append(f"{i}. {status} {item['task']}")
        await update.message.reply_text("\n".join(msg_lines))

    elif command == "done":
        if len(args) < 2 or not args[1].isdigit():
            await update.message.reply_text("❗ Укажи номер задачи, чтобы отметить выполненной.")
            return
        index = int(args[1]) - 1
        if 0 <= index < len(user_todos):
            user_todos[index]["done"] = True
            save_todos(todos)
            await update.message.reply_text(f"✔ Задача {index+1} отмечена выполненной.")
        else:
            await update.message.reply_text("❌ Неверный номер задачи.")

    elif command == "delete":
        if len(args) < 2 or not args[1].isdigit():
            await update.message.reply_text("❗ Укажи номер задачи для удаления.")
            return
        index = int(args[1]) - 1
        if 0 <= index < len(user_todos):
            removed = user_todos.pop(index)
            save_todos(todos)
            await update.message.reply_text(f"🗑 Задача удалена: {removed['task']}")
        else:
            await update.message.reply_text("❌ Неверный номер задачи.")

    else:
        await update.message.reply_text("Неизвестная подкоманда. Используй add / list / done / delete")
