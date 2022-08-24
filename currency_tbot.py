from aiogram import Dispatcher, executor, Bot, types
import os
import asyncio
import logging
from queries import *
from requests_banks import *
# unique id for telegram bot
TOKEN = 'TELEGRAM_BOT_TOKEN'
# banks list
banks = {'rico': ge_rico_rates,
		 'state': ge_state_rates,
		 'tbc': ge_tbc_rates,
		 'georgiabank': ge_georgiabank_rates,
		 'mbc': ge_mbc_rates,
		 'basis': ge_basis_rates,
		 'crystal': ge_crystal_rates,
		 'tinkoff': ru_tinkoff_rates,
		 'isbank': tr_isbank_rates,
		 'trabzon': tr_trabzon_rates,
		 'prior': by_prior_rates
		 }

# function for add new data into database
async def add_new_data_to_db():
    while True:
        for k,v in banks.items():
            insert_data_to_db(v)
        print('new data added into db succesfully')
        await asyncio.sleep(86400)

# function for update data 
async def update_data_in_db():
	while True:
		await asyncio.sleep(1800)
		for k,v in banks.items():
			update_data_db(v)
		print('db updated succesfully')

# add and update data for teleram bot 
async def bot_adding_updating(dispatcher: Dispatcher):
	asyncio.create_task(add_new_data_to_db())
	asyncio.create_task(update_data_in_db())

# commands for telegram bot
async def command_usd_buy(message: types.Message):
	command = select_data_from_db('usd_sell')
	await message.reply(command)


async def command_usd_sell(message: types.Message):
	command = select_data_from_db('usd_buy')
	await message.reply(command)


async def command_euro_buy(message: types.Message):
	command = select_data_from_db('euro_sell')
	await message.reply(command)


async def command_euro_sell(message: types.Message):
	command = select_data_from_db('euro_buy')
	await message.reply(command)


async def command_lira_buy(message: types.Message):
	command = select_data_from_db('lira_sell')
	await message.reply(command)

''
async def command_lira_sell(message: types.Message):
	command = select_data_from_db('lira_buy')
	await message.reply(command)


async def command_foreign_banks(message: types.Message):
	command = select_data_foreign_banks_db()
	await message.reply(command)

commands_list = [(command_usd_buy, 'usd_buy'),
				 (command_usd_sell, 'usd_sell'),
				 (command_euro_buy, 'euro_buy'),
				 (command_euro_sell, 'euro_sell'),
				 (command_lira_buy, 'lira_buy'),
				 (command_lira_sell, 'lira_sell'),
				 (command_foreign_banks, 'foreign_banks')]

# creating and starting telegram bot
def create_command_to_bot():
	dp = Dispatcher(Bot(token=TOKEN))
	# bot endpoints block:
	for command in commands_list:
		dp.register_message_handler(
			command[0],
			commands=[command[1]]
		)
	# start bot
	executor.start_polling(dp, skip_updates=True, on_startup=bot_adding_updating)


if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)
	create_command_to_bot()
