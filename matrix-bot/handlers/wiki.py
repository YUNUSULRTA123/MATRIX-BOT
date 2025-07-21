import wikipedia
from telegram import Update
from telegram.ext import ContextTypes

wikipedia.set_lang("ru")  # можно изменить на 'en'

async def wiki_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠️ Введите запрос. Пример: /wiki Python")
        return

    query = " ".join(context.args)
    try:
        summary = wikipedia.summary(query, sentences=3)
        await update.message.reply_text(f"📚 *{query}*:\n{summary}", parse_mode="Markdown")
    except wikipedia.exceptions.DisambiguationError as e:
        await update.message.reply_text(f"⚠️ Слишком много вариантов. Уточни: {e.options[:5]}")
    except wikipedia.exceptions.PageError:
        await update.message.reply_text("❌ Страница не найдена.")
    except Exception as e:
        await update.message.reply_text(f"⚠️ Ошибка: {str(e)}")
