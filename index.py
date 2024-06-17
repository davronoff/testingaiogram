import aiogram
import logging
import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold


db = Dispatcher()


@db.message(CommandStart())
async def cmd_start(msg: types.Message) -> None:

  """Process the command start"""

  replay_text = f'Hello, {hbold(msg.from_user.first_name)}'

  await msg.answer(
    text=replay_text, 
    parse_mode='HTML'
  )


async def main() -> None:
  bot = Bot("7311726469:AAHD5xOq6EwAsd6ZjZ3o7g-ao67qzmoVh3I")

  await db.start_polling(bot)

if __name__ == "__main__":
  asyncio.run(main())
