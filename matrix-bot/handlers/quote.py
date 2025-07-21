import random
from telegram import Update
from telegram.ext import ContextTypes

QUOTES = [
    "Будь собой — прочие роли уже заняты. — Оскар Уайльд",
    "Великие дела начинаются с малого.",
    "Если ты идёшь через ад — не останавливайся. — Уинстон Черчилль",
    "Мечты не работают, пока не работаешь ты.",
    "Ничего не бойся. Это просто жизнь.",
    "Терпение — ключ к успеху."
]

async def quote_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quote = random.choice(QUOTES)
    await update.message.reply_text(quote)
