from aiogram import Bot, Dispatcher, executor, types
from kb_client import kb_client
from main import nameZP, skills

TOKEN = "5627555066:AAE-EeCWJxIhmmr9ZGAv1Wd92hRIvEur6Vo"

bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Hello, i can find work for you!',
                           reply_markup=kb_client)

@dp.message_handler(commands=['Works'])
async def cmd_works(message: types.Message):
    name, zp =nameZP()
    list_skills = skills()
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'''{name}
{zp}
SKILLS: {list_skills}''')

executor.start_polling(dp, skip_updates=True)