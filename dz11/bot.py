import time
import logging

from aiogram import Bot, Dispatcher, executor, types

TOKEN ='5628087940:AAFLfnU5-kFprVzAgfNyOO0EnxmzoMT1CVI'
MESSAGE = 'Программировал ли ты сегодня? {}'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
  user_id = message.from_user.id
  user_name = message.from_user.first_name
  user_full_name = message.from_user.full_name
  logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')

  await message.reply(f"Привет, {user_full_name}!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отправлю этот текст тебе в ответ!")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)



    for i in range(10):
      time.sleep(60*60*24)
      await bot.send_message(user_id, MESSAGE.format(user_name))


if __name__ == '__main__':
  executor.start_polling(dp)



