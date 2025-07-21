import requests

async def weather_handler(update, context):
    if not context.args:
        await update.message.reply_text("Пожалуйста, укажи город. Пример: /weather Москва")
        return

    city = " ".join(context.args)
    url = f"https://wttr.in/{city}?format=3"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            await update.message.reply_text(response.text)
        else:
            await update.message.reply_text("Не удалось получить данные о погоде.")
    except Exception as e:
        await update.message.reply_text("Ошибка при получении погоды.")
