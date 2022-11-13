from aiogram import Bot, Dispatcher, executor, types

#bot = Bot(token="5433165964:AAF2wLK0m95vke2hjLKLEFRNe__XRY123M8")
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

