import logging
from aiogram import Bot, Dispatcher, executor, types
from requests_banks import *
#from queries import *

# Объект бота
bot = Bot(token="5286487843:AAEiloLTW3WW4nvSdsJwRwYFijiZbe8PqvQ")
# Диспетчер для бота
dp = Dispatcher(bot)

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Хэндлер на команду /buy_dollar
@dp.message_handler(commands="buy_usd")
async def cmd_buy_dollar(message: types.Message):
    command = get_rates('usd_buy')
    await message.reply(command)
    

# Хэндлер на команду /sell_dollar
@dp.message_handler(commands="sell_usd")
async def cmd_sell_dollar(message: types.Message):
    command = get_rates('usd_sell')
    await message.reply(command)


# Хэндлер на команду /buy_euro
@dp.message_handler(commands="buy_euro")
async def cmd_buy_euro(message: types.Message):
    command = get_rates('euro_buy')
    await message.reply(command)
    

# Хэндлер на команду /sell_euro
@dp.message_handler(commands="sell_euro")
async def cmd_sell_euro(message: types.Message):
    command = get_rates('euro_sell')
    await message.reply(command)


# Хэндлер на команду /buy_lira
@dp.message_handler(commands="buy_lira")
async def cmd_buy_lira(message: types.Message):
    command =get_rates('lira_buy')
    await message.reply(command)
    

# Хэндлер на команду /sell_lira
@dp.message_handler(commands="sell_lira")
async def cmd_sell_lira(message: types.Message):
    command = get_rates('lira_sell')
    await message.reply(command)
    
# Хэндлер на команду /f_buy_usd
@dp.message_handler(commands="f_buy_usd")
async def cmd_buy_lira(message: types.Message):
    command =get_rates('buy_usd', 'ww')
    await message.reply(command)

# Хэндлер на команду /f_sell_usd
@dp.message_handler(commands="foreign_banks")
async def cmd_buy_lira(message: types.Message):
    command = foreign_banks()
    await message.reply(command)

"""@dp.message_handler(commands="get_sql")
async def cmd_buy_lira(message: types.Message):
    command = select_db()
    await message.reply(command) """

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)