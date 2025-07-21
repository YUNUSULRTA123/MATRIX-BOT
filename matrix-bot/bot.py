import os
from dotenv import load_dotenv
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
)
from handlers.start import start_handler
from handlers.calc import calc_handler
from handlers.quote import quote_handler
from handlers.note import note_handler
from handlers.todo import todo_handler
from handlers.convert import convert_handler
from handlers.music import music_handler
from handlers.weather import weather_handler
from handlers.remind import remind_handler
from handlers.translate import translate_handler
from handlers.calendar import addevent_handler, events_handler
from handlers.time import time_handler, timezone_handler
from handlers.clear import clear_handler
from handlers.meditate import meditate_handler
from handlers.quiz import quiz_start, quiz_answer, quiz_cancel, ANSWER
from handlers.fun import joke_handler, fact_handler, cat_handler, dog_handler, advice_handler
from handlers.shorten import shorten_handler
from handlers.ipinfo import ip_handler
from handlers.ascii import ascii_handler
from handlers.qr import qr_handler
from handlers.download import download_handler
from handlers.wiki import wiki_handler
from handlers.ask import ask_handler 

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

quiz_conv = ConversationHandler(
    entry_points=[CommandHandler("quiz", quiz_start)],
    states={ANSWER: [MessageHandler(filters.TEXT & ~filters.COMMAND, quiz_answer)]},
    fallbacks=[CommandHandler("cancel", quiz_cancel)],
)

app.add_handler(CommandHandler("start", start_handler))
app.add_handler(CommandHandler("calc", calc_handler))
app.add_handler(CommandHandler("quote", quote_handler))
app.add_handler(CommandHandler("note", note_handler))
app.add_handler(CommandHandler("todo", todo_handler))
app.add_handler(CommandHandler("convert", convert_handler))
app.add_handler(CommandHandler("music", music_handler))
app.add_handler(CommandHandler("weather", weather_handler))
app.add_handler(CommandHandler("remind", remind_handler))
app.add_handler(CommandHandler("translate", translate_handler))
app.add_handler(CommandHandler("addevent", addevent_handler))
app.add_handler(CommandHandler("events", events_handler))
app.add_handler(CommandHandler("time", time_handler))
app.add_handler(CommandHandler("timezone", timezone_handler))
app.add_handler(CommandHandler("clear", clear_handler))
app.add_handler(CommandHandler("meditate", meditate_handler))
app.add_handler(quiz_conv)
app.add_handler(CommandHandler("joke", joke_handler))
app.add_handler(CommandHandler("fact", fact_handler))
app.add_handler(CommandHandler("cat", cat_handler))
app.add_handler(CommandHandler("dog", dog_handler))
app.add_handler(CommandHandler("advice", advice_handler))
app.add_handler(CommandHandler("shorten", shorten_handler))
app.add_handler(CommandHandler("ip", ip_handler))
app.add_handler(CommandHandler("ascii", ascii_handler))
app.add_handler(CommandHandler("qr", qr_handler))
app.add_handler(CommandHandler("download", download_handler))
app.add_handler(CommandHandler("wiki", wiki_handler))
app.add_handler(CommandHandler("ask", ask_handler))  

if __name__ == "__main__":
    print("Бот запущен...")
    # 🚀 Запуск бота
    app.run_polling()