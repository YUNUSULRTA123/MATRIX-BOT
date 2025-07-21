import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode
from dotenv import load_dotenv
import traceback

# Загружаем переменные окружения (.env)
load_dotenv()

# Настройка Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

# Разбивка длинного текста
def split_message(text, max_length=4096):
    parts = []
    while len(text) > max_length:
        split_at = text.rfind('\n', 0, max_length)
        if split_at == -1:
            split_at = max_length
        parts.append(text[:split_at])
        text = text[split_at:].lstrip()
    parts.append(text)
    return parts

# Основной обработчик команды /ask
async def ask_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = " ".join(context.args)

    if not user_input:
        await update.message.reply_text(
            "❗ Пожалуйста, задай вопрос: `/ask твой вопрос`",
            parse_mode=ParseMode.MARKDOWN
        )
        return

    try:
        # Генерация ответа
        response = model.generate_content(user_input)
        answer = response.text.strip()

        if not answer:
            await update.message.reply_text("🤔 Я не смог придумать ответ. Попробуй переформулировать вопрос.")
            return

        # Отправка ответа по частям
        for part in split_message(answer):
            await update.message.reply_text(part, parse_mode=ParseMode.MARKDOWN)

    except Exception:
        print("🔥 Ошибка Gemini:")
        print(traceback.format_exc())
        await update.message.reply_text("⚠️ Произошла ошибка при получении ответа. Попробуй позже.")
