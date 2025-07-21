from datetime import datetime
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz
from telegram import Update
from telegram.ext import ContextTypes

geolocator = Nominatim(user_agent="telegram_time_bot")
tf = TimezoneFinder()

async def time_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Использование: /time <город>\nПример: /time Москва")
        return

    city = " ".join(context.args)
    try:
        location = geolocator.geocode(city)
        if not location:
            await update.message.reply_text("❗ Город не найден. Попробуй другой.")
            return

        timezone_str = tf.timezone_at(lat=location.latitude, lng=location.longitude)
        if not timezone_str:
            await update.message.reply_text("⏳ Не удалось определить временную зону.")
            return

        timezone = pytz.timezone(timezone_str)
        local_time = datetime.now(timezone)
        time_formatted = local_time.strftime("%d.%m.%Y %H:%M")

        await update.message.reply_text(f"🕒 Текущее время в городе *{city.title()}*:\n{time_formatted}",
                                        parse_mode="Markdown")

    except Exception as e:
        await update.message.reply_text(f"Произошла ошибка: {e}")

async def timezone_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "Использование: /timezone <город>\nПример: /timezone Лондон"
        )
        return

    city = " ".join(context.args).strip(" ,.")
    try:
        location = geolocator.geocode(city)
        if not location:
            await update.message.reply_text("❗ Город не найден. Попробуй другой.")
            return

        timezone_str = tf.timezone_at(lat=location.latitude, lng=location.longitude)
        if not timezone_str:
            await update.message.reply_text("Не удалось определить временную зону.")
            return

        await update.message.reply_text(
            f"🌍 Временная зона для *{city.title()}*:\n`{timezone_str}`",
            parse_mode="Markdown"
        )

    except Exception as e:
        await update.message.reply_text(f"Произошла ошибка: {e}")
