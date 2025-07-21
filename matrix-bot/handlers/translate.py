import aiohttp
import logging

logger = logging.getLogger(__name__)

LANGUAGES = {
    "en": "Английский",
    "ru": "Русский",
    "es": "Испанский",
    "fr": "Французский",
    "de": "Немецкий",
    "it": "Итальянский",
    "tr": "Турецкий",
    "zh": "Китайский",
    "ja": "Японский"
}

def get_supported_languages():
    return "\n".join([f"{code} — {name}" for code, name in LANGUAGES.items()])

async def translate_handler(update, context):
    if len(context.args) < 2:
        await update.message.reply_text(
            "❗ Формат: /translate <язык> <текст>\n"
            "Пример: /translate en Привет, как дела?\n\n"
            "🌐 Поддерживаемые языки:\n" +
            get_supported_languages()
        )
        return

    target_lang = context.args[0].lower()
    if target_lang not in LANGUAGES:
        await update.message.reply_text(
            f"⚠️ Язык '{target_lang}' не поддерживается.\n\n"
            "✅ Поддерживаемые языки:\n" + get_supported_languages()
        )
        return

    text = " ".join(context.args[1:])
    url = "https://translate.astian.org/translate"
    payload = {
        "q": text,
        "source": "auto",
        "target": target_lang,
        "format": "text"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=payload, headers=headers, timeout=10) as response:
                if response.status != 200:
                    error_text = await response.text()
                    logger.error(f"API error: {response.status} — {error_text}")
                    await update.message.reply_text(
                        f"⚠️ Сервис вернул ошибку {response.status}.\n"
                        f"{error_text[:300]}"
                    )
                    return

                result = await response.json()
                translated = result.get("translatedText")

                if translated:
                    await update.message.reply_text(f"📤 Перевод: {translated}")
                else:
                    logger.warning(f"Пустой ответ: {result}")
                    await update.message.reply_text("⚠️ Перевод не получен.")
    except Exception as e:
        logger.exception("Ошибка при обращении к API")
        await update.message.reply_text(f"❌ Ошибка при подключении к сервису перевода:\n{e}")
