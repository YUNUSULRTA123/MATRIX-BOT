from telegram import Update
from telegram.ext import ContextTypes

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """Привет! 👋 Я твой универсальный помощник. Вот что я умею:\n
/start - Приветствие и помощь 📢  
/calc - Калькулятор 🧮  
/quote - Случайная цитата 📝  
/note - Создать заметку 🗒️  
/todo - Список дел 📋  
/convert - Конвертер валют 💸  
/music - Музыка по запросу 🎵  
/weather - Погода по городу ⛅  
/remind - Напоминание по времени ⏰  
/translate - Перевод текста 🌐
/addevent и /events - добавить и постмотреть собитие(я) 📅
/time - Посмотреть на время в любых регионах 🕒
/timezone - узнайте ваш часовой пояс по времени 🌍
/clear - Очищать последние 10 сообщений (если возможно) 🗑️
/meditate - сделайте вдох и выдох за пару секунд 💨
/quiz и /cancel - сыграть или остоновить викторину 🧠
/joke - Случайная шутка 🤣
/fact - Интересный факт 🤔
/cat - Фото кота 😺 
/dog - Фото собаки 🐶
/advice - Полезный совет ✔️
/shorten - Сократить ссылку 🔗
/ip - показывает информацию о вашем IP-адресе 🛜
/ask - ответ от ИИ
/wiki - ответ от Википедии\n
Если нужна помощь обращайся - @yunus_pro_hour_of_code"""
    )