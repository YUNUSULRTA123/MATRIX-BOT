from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler, MessageHandler, filters

QUESTION, ANSWER = range(2)

quiz_questions = [
    {
        "q": "Назовите год подписания Декларации независимости США.",
        "a": ["1776"]
    },
    {
        "q": "Что такое 'энтропия' в термодинамике?",
        "a": ["мера беспорядка", "мера хаоса", "степень беспорядка"]
    },
    {
        "q": "Кто написал оперу 'Кармен'?",
        "a": ["жорж бизе", "бизе"]
    },
    {
        "q": "Какое химическое соединение является основой жизни на Земле?",
        "a": ["углерод", "карбон"]
    },
    {
        "q": "В какой стране находится гора Килиманджаро?",
        "a": ["танзания"]
    },
    {
        "q": "Как называется самый большой океан на Земле?",
        "a": ["тихий океан", "тихий"]
    },
    {
        "q": "Что изучает наука 'эпистемология'?",
        "a": ["теория познания", "философия знания"]
    },
    {
        "q": "Какова формула площади круга?",
        "a": ["πr²", "пи r квадрат", "пи*r*r"]
    },
    {
        "q": "Кто создал теорию относительности?",
        "a": ["эйнштейн", "альберт эйнштейн"]
    },
    {
        "q": "Что такое квантовая запутанность?",
        "a": ["связь частиц на расстоянии", "корреляция квантовых состояний"]
    },
]

async def quiz_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["quiz_index"] = 0
    question = quiz_questions[0]["q"]
    await update.message.reply_text(f"Викторина началась! Вопрос 1:\n{question}")
    return ANSWER

async def quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_answer = update.message.text.lower().strip()
    index = context.user_data.get("quiz_index", 0)
    correct_answers = quiz_questions[index]["a"]

    if any(user_answer == ans for ans in correct_answers):
        await update.message.reply_text("✅ Правильно!")
    else:
        correct = correct_answers[0].capitalize()
        await update.message.reply_text(f"❌ Неправильно. Правильный ответ: {correct}.")

    index += 1
    if index >= len(quiz_questions):
        await update.message.reply_text("🎉 Викторина окончена! Спасибо за участие.")
        return ConversationHandler.END

    context.user_data["quiz_index"] = index
    question = quiz_questions[index]["q"]
    await update.message.reply_text(f"Вопрос {index+1}:\n{question}")
    return ANSWER

async def quiz_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Викторина отменена.")
    return ConversationHandler.END
