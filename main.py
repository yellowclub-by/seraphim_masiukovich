import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
Token = "8036464450:AAGHf2rh8uUkKCdtGYDqQH2jrWcL9EB850I"


bot = Bot(token = Token)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message:types.Message):
    await message.answer("Добро пожаловать!")
@dp.message(Command("catalog"))
async def catalog(message:types.Message):
    await message.answer("каталог:")

@dp.message(Command("korzinka"))
async def korzinka(message:types.Message):
    await message.answer("корзина состоит из:")

@dp.message(Command("o_nas"))
async def o_nas(message: types.Message):
    await message.answer("создатель:SeraphimTech, бот сделан по приколу!!!")
@dp.message()
async def echo(message: types.Message):
    await message.answer(f'Привет, @{message.from_user.username}, бот в разработке!!!')
    await message.answer(f'id {message.from_user.id}')
    await message.answer(f'first name {message.from_user.first_name}')
    user_text = message.text
    await message.answer(user_text)
async def main():
    print("bot started")
    await dp.start_polling(bot)





asyncio.run(main())