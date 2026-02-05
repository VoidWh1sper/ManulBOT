import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "BOT_TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

MANUL_PHOTOS = [
    f"https://loremflickr.com/800/600/manul,cat?lock={i}" 
    for i in range(1, 501)
]

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Привет! Я бот-манул. Просто напиши 'манул' или 'manul'!")

@dp.message()
async def handle_message(message: types.Message):
    if message.text:
        text_lower = message.text.lower()
        if "манул" in text_lower or "manul" in text_lower:
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
