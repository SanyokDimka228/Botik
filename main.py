from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.exceptions import MessageNotModified
from config_bot import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

buttons = [InlineKeyboardButton(text="Мем", callback_data="button_1")]
kbd = InlineKeyboardMarkup(row_width=2)
for button in buttons:
    kbd.insert(button)

kbd_reply = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=[
    [KeyboardButton(text="Привіт"), KeyboardButton(text="Location", request_location=True)],
])



@dp.message_handler(Command(['start']))
async def say_hello(message: types.Message):
    await message.answer(text="Вітаю вас у боті мемів\nПісля вибору теми напишіть 'Мем', або 'Бувай' щоб вийти з програми", reply_markup=kbd)

@dp.message_handler(Text(contains=['Мем']))
async def start(message: types.Message):
    print("Мем")
    with open('photo.png', 'rb') as file:
        await message.answer_photo(photo=file, caption="Ось ваш мем)")

executor.start_polling(dp)


# async def mood(message: types.Message):
#     await message.reply(text = "Окей)", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(contains=['Бувай']))
async def mood(message: types.Message):
    await message.reply(text = "Бай бай", reply_markup=types.ReplyKeyboardRemove())


# @dp.callback_query_handler(Text(startswith=""))
# async def process_button(callback: types.CallbackQuery):
#     await callback.answer()
#     button_number = callback.data.split("_")[1]
#     await callback.message.answer(text=f"Ви натиснули на кнопку {button_number}", reply_markup=kbd_reply)


if __name__ == '__main__':
    executor.start_polling(dp)