from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ChatMemberStatus

async def clear_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat

    try:
        # Удаляем саму команду /clear, если бот может
        try:
            await context.bot.delete_message(chat_id=chat.id, message_id=update.message.message_id)
        except:
            pass  # в личке может не получиться

        if chat.type == "private":
            await context.bot.send_message(chat.id, "Я бы рад удалить сообщения, но Telegram сказал «ни-ни» ☠️")
            return

        # Для групп — проверка прав
        bot_member = await context.bot.get_chat_member(chat.id, context.bot.id)
        if bot_member.status != ChatMemberStatus.ADMINISTRATOR:
            await context.bot.send_message(chat.id, "❗ Мне нужны права администратора для удаления сообщений.")
            return

        if not getattr(bot_member, "can_delete_messages", False):
            await context.bot.send_message(chat.id, "❗ У меня нет разрешения на удаление сообщений.")
            return

        # Удаляем последние 10 сообщений (в группе)
        count = 0
        for i in range(update.message.message_id - 1, update.message.message_id - 11, -1):
            try:
                await context.bot.delete_message(chat.id, i)
                count += 1
            except:
                continue

    except Exception as e:
        await context.bot.send_message(chat.id, f"🚫 Ошибка: {e}")
