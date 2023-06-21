from aiogram import Dispatcher
from aiogram.types import Message


async def send_echo(message: Message):
    await message.answer(f'回声 {message.text}')


def register_echo_handler(dp: Dispatcher):
    dp.register_message_handler(send_echo)