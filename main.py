import asyncio
import re
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "TELEGRAM_TOKEN"

MANUL_PHOTOS = [
    "https://yandex-images.clstorage.net/z5oY2w148/5ae631jMS/ore13bIPX2jy4YIn8IOmCP6ugiwKOheCvUjEpYJz3cTeHrBRj-L4SuIJ6aNgFkm4h0YZx9NlnDMDV3uH_847e8ey7NjzHiZ08vXTC9mzzji--7JZBm8f5q1VoJTKlzAVG9pJpAInIOs7IKXWZSf0DOZG8K7ySUji-j_u27O3ij46q2XtJhsCNOpNB6s8kzKUiqeWCIZnh69VRHmJFlMASavyqZTGV4RjD2CoIhm3wKG-OqwapiXIel5j2h8jG75GhtuVEX6jInB2lR-3mEt2lFKD6gj-v3P7cUA99b6v1C3TsqlQch_cl6-ItMq9qzDJ7lLcxqLZIOJyA3KrF-OuSpbz8RXiHzL8nkHb30AjLsDSmw7Qhrc__21cgX2eg8CtU_KtwEYHuJub5OQyCVs0bfae0AIe7SxGRq964x9rKspyQ-FRVgMaMMIldztAvzY4Svd-xLoPM_dd3D1ZntskVYfiLVz6Y_Cf1_Q80oUjPN1-VvBKDhVAyto7UqOHG5Y2Yq-5wZr3JthuqQ93oDuqBM6XFijSz6cXefT9zb5XrMGvkh0ALjsA86vkqCrxfzSRUsYges4NDDJ21-bb09sS-vLXKQVm43aYTmkPP3S3ltiOU_64hlMXYxV4cYUSf2jJV4rlSHbLqH8LfEBmbasgEbbC_JqWZUCK-qOyQ0MvgrqWT_2tbkM25Ib91zekP14ccgN6JKK3A38J8O2J5uOUuQf-cQjyH-jzXxy0opHXMN22gqxeHsnscoa__keHa-b2kiP1zS6bRhD6_Zej1IOyOK4r2iySL2uPYdC9uY73UKWrMtUgLrsESweERA6BvwDdyvok3nLNFDoOp9IL299ajpoj_e2io7ro_iHrJziXNrh-i644Uou_EylM2YU2w_AJE8ppiMJHZAvjBLh2kTMsMQ46NC5yJZyqstP2H1ebAvKq0_21qu9y-KJ1J9-YwxbAMteOsFJT62dpZN3hFqdc",
    "https://i.pinimg.com/736x/f6/cc/be/f6ccbe32d4108f82aa42aa1fa29baad1.jpg",
    "https://i.pinimg.com/originals/73/c6/39/73c639c2b5ecd88811043953322e261f.jpg"
]

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def handle_message(message: types.Message):
    if message.text:
        text = message.text.lower()
        pattern = re.compile(r'манул|manul', re.IGNORECASE)
        if pattern.search(text):
            await message.answer_photo(random.choice(MANUL_PHOTOS))

async def main():
    print("✅ ManulBOT запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
