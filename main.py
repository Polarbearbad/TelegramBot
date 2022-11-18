from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram import executor
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def gretting(message: Message):
    await bot.send_message(message.from_user.id, "Hello How can I help You")


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
