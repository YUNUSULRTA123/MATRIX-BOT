from telegram import Update
from telegram.ext import ContextTypes

rates = {
    "USD": 1.0,
    "EUR": 0.92,
    "RUB": 90.0,
    "GBP": 0.78,
    "AZN": 1.7,
    "BTC": 0.000016,
}

# Символы валют
symbols = {
    "USD": "$",
    "EUR": "€",
    "RUB": "₽",
    "GBP": "£",
    "AZN": "₼",
    "BTC": "₿",
}

# Хэндлер конвертации
async def convert_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "Пожалуйста, укажите сумму и валюты.\n"
            "Пример: /convert 100 USD RUB\n"
            "Поддерживаемые валюты: " + ", ".join(rates.keys())
        )
        return

    try:
        args = context.args
        if len(args) != 3:
            await update.message.reply_text(
                "Неверный формат команды.\nИспользование: /convert <сумма> <из> <в>\n"
                "Пример: /convert 100 USD RUB"
            )
            return

        amount_str, from_currency, to_currency = args
        amount = float(amount_str.replace(",", "."))

        if amount < 0:
            await update.message.reply_text("Сумма должна быть положительным числом.")
            return

        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in rates or to_currency not in rates:
            await update.message.reply_text(
                "Одна или обе валюты не поддерживаются.\nПоддерживаемые валюты: " +
                ", ".join(rates.keys())
            )
            return

        if rates[from_currency] == 0:
            await update.message.reply_text("Ошибка: курс исходной валюты равен нулю.")
            return

        # Конвертация
        converted = amount / rates[from_currency] * rates[to_currency]
        from_symbol = symbols.get(from_currency, from_currency)
        to_symbol = symbols.get(to_currency, to_currency)

        await update.message.reply_text(
            f"{amount:,.2f} {from_symbol} ({from_currency}) = "
            f"{converted:,.2f} {to_symbol} ({to_currency})"
        )

    except ValueError:
        await update.message.reply_text("Ошибка: сумма должна быть числом.")
    except Exception as e:
        await update.message.reply_text(f"Неожиданная ошибка: {e}")
