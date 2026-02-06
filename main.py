import asyncio
import random
import json
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "TOKEN_BOT"

bot = Bot(token=TOKEN)
dp = Dispatcher()

MANUL_PHOTOS = [
    f"https://loremflickr.com/800/600/manul,cat?lock={i}" 
    for i in range(1, 501)
]

BAD_MANUL_WORDS ={
  "bad_words": [
    "манул блядь",
    "манул мудак",
    "манул говно",
    "манул пидор",
    "манул урод",
    "манул дурак",
    "manul fuck",
    "manul shit",
    "manul asshole",
    "manul идиот",
    "манулы бляди",
    "манулы мудаки",
    "манулы говно",
    "манулы пидоры",
    "манулы уроды",
    "манулы дураки"
  ],
  "evil_responses": [
    "Манул обиделся и ушел 😠",
    "Не оскорбляй манула! 😾",
    "Манул недоволен твоими словами 😡",
    "Такие слова обижают манулов 🐾",
    "Манул разозлился и показал когти!",
    "Фу, как некультурно! Манул расстроен 😿"
  ]
}

with open('bad_manul_words.json', 'w', encoding='utf-8') as f:
    json.dump(BAD_MANUL_WORDS, f, ensure_ascii=False, indent=2)

with open('bad_manul_words.json', 'r', encoding='utf-8') as f:
    BAD_WORDS_DATA = json.load(f)
    BAD_WORDS = BAD_WORDS_DATA["bad_words"]
    EVIL_RESPONSES = BAD_WORDS_DATA["evil_responses"]

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Привет! Я бот-манул. Просто напиши 'манул' или 'manul'!")

@dp.message()
async def handle_message(message: types.Message):
    if message.text:
        text_lower = message.text.lower()
        is_bad_word = False
        for bad_word in BAD_WORDS:
            if bad_word in text_lower:
                is_bad_word = True
                break
        
        if is_bad_word:
            evil_response = random.choice(EVIL_RESPONSES)
            try:
                await message.reply_photo(
                    photo=evil_photo,
                    caption=f"⚠️ {evil_response}"
                )
            except:
                await message.answer(f"⚠️ {evil_response}")

        elif "манул" in text_lower or "manul" in text_lower:
            random_photo = random.choice(MANUL_PHOTOS)
            
            try:
                await message.reply_photo(photo=random_photo)
            except Exception as e:
                print(f"Ошибка при отправке фото: {e}")
                await message.answer("Ой, манул спрятался! Попробуйте еще раз.")

async def main():
    print("Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
