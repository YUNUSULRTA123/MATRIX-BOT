from telegram import Update
from telegram.ext import ContextTypes

async def calc_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Пример: /calc 2 + 2 * 3")
        return

    expression = " ".join(context.args)
    allowed = "0123456789+-*/(). "

    if any(c not in allowed for c in expression):
        await update.message.reply_text("Ошибка: недопустимые символы")
        return

    try:
        result = eval(expression)
        await update.message.reply_text(f"Ответ: {result}")
    except Exception as e:
        await update.message.reply_text(f"Ошибка вычисления: {e}")
