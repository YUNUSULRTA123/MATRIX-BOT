import aiohttp
import random
from telegram import Update
from telegram.ext import ContextTypes

async def joke_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://official-joke-api.appspot.com/random_joke"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                joke = f"{data['setup']}\n{data['punchline']}"
                await update.message.reply_text(joke)
            else:
                await update.message.reply_text("Не удалось получить шутку.")

async def fact_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                await update.message.reply_text(data['text'])
            else:
                await update.message.reply_text("Не удалось получить факт.")

async def cat_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://api.thecatapi.com/v1/images/search"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                await update.message.reply_photo(data[0]['url'])
            else:
                await update.message.reply_text("Не удалось загрузить кота.")

async def dog_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://dog.ceo/api/breeds/image/random"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                await update.message.reply_photo(data['message'])
            else:
                await update.message.reply_text("Не удалось загрузить собаку.")

async def advice_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://api.adviceslip.com/advice"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                await update.message.reply_text(data['slip']['advice'])
            else:
                await update.message.reply_text("Не удалось получить совет.")
