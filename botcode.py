from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from buttons import button, button1, bm, bP, bP1
from mybot.api import createuser, createariza, createkerio, createpochta
import logging
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ParseMode
from aiogram.utils import executor
import requests
from datetime import datetime
API_TOKEN = '6524167059:AAFNtUxKDL-m8ttpsqPVvVIAxtbhPVlWCus'
# Configure logging



# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot, storage = MemoryStorage())

logging.basicConfig(level=logging.INFO)


class Form(StatesGroup):
    name = State()
    kaf = State()
    xona = State()
    text = State()


class KForm(StatesGroup):
    fullname = State()
    department = State()
    rank = State()
    login = State()
    parol = State()


class PForm(StatesGroup):
    fullname = State()
    department = State()
    rank = State()


but = types.KeyboardButton("Telefon raqamingni jo'natish", request_contact=True)
button_markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(but)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    response = requests.get("http://127.0.0.1:8000/api/myv/botusers")
    data = response.json()
    a=False
    for i in data:

        if str(message.from_user.id) == i['user_id']:

            a = True
            break
    if a==True:
        await message.answer("Assalomu aleykum! Namangan Muxandislik qurilish instituti \nRaqamli Ta'lim Texnologiyalari Markazi botiga Xush kelibsiz",reply_markup=button)
    else:
        await message.answer(
            "Telefon raqamingizni yuboring",reply_markup=button_markup)


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def handle_contact(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    phone_number = message.contact.phone_number
    # Ma'lumotlarni saqlash funksiyasini chaqirish
    createuser(username, first_name, user_id, phone_number)
    response = requests.get("http://127.0.0.1:8000/api/myv/botusers")
    data = response.json()
    user_exists = any(str(user_id) == i['user_id'] for i in data)

    if user_exists:
        await send_welcome(message)


@dp.message_handler(lambda message: message.text == '🖥 Texnik xizmat ko`rsatish 🖥' and message.content_type == 'text')
async def start(message: types.Message):
    await Form.name.set()
    await message.answer("Assalomu alaykum! Ismingizni kiriting.", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(bm))


@dp.message_handler(lambda message: message.text == '🔙 Bosh menyuga qaytish', state="*")
async def back_to_start(message: Message, state: FSMContext):
    await state.finish()
    await send_welcome(message)


@dp.message_handler(state=Form.name)
async def receive_name(message: Message, state: FSMContext):
    user_name = message.text
    await state.update_data(name=user_name)
    print({user_name},' ',{Form.name})
    await Form.next()
    await message.reply("Bo'lim yoki kafedrangizni tanlang", reply_markup=button1)


@dp.message_handler(state=Form.kaf)
async def receive_kaf(message: Message, state: FSMContext):
    kafl = message.text
    await state.update_data(kaf=kafl)
    print({kafl}, ' ', {Form.kaf})
    await Form.next()
    await message.reply("Bino, qavat va xona raqamini kiriting : \nMasalan 1-bino 2-qavat 213-xona \n1-bino 3-qavat Karupsiyaga qarshi kurash bo'limi.", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(bm))


@dp.message_handler(state=Form.xona)
async def receive_xona(message: Message, state: FSMContext):
    xona = message.text
    await state.update_data(xona=xona)
    print({xona}, ' ', {Form.xona})
    await Form.next()
    await message.reply("Muommoyingizni batafsil yozing: \nMasalan Windows aktivatsiya qilish", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(bm))


@dp.message_handler(state=Form.text)
async def receive_text(message: Message, state: FSMContext):
    txt = message.text
    user_data = await state.get_data()
    user_id = message.from_user.id
    createariza(user_id, user_data['name'], user_data['kaf'], user_data['xona'], txt)
    print({txt}, ' ')
    await state.finish()
    await message.reply("Ariza muvaffaqiyatli qabul qilindi!", reply_markup=button)


@dp.message_handler(lambda message: message.text == '🌐 Wi-Fi uchun login/parol olish 🌐' and message.content_type == 'text')
async def start(message: types.Message):
    await KForm.fullname.set()
    await message.answer("Assalomu alaykum! Ismingizni kiriting.", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(bm))


@dp.message_handler(lambda message: message.text == '🔙 Bosh menyuga qaytish', state="*")
async def back_to_start(message: Message, state: FSMContext):
    await state.finish()
    await send_welcome(message)


@dp.message_handler(state=KForm.fullname)
async def fullname(message: Message, state: FSMContext):
    user_name = message.text
    await state.update_data(fullname=user_name)
    await KForm.next()
    await message.reply("Bo'lim yoki kafedrangizni tanlang", reply_markup=button1)


@dp.message_handler(state=KForm.department)
async def department(message: Message, state: FSMContext):
    kafl = message.text
    await state.update_data(department=kafl)
    await KForm.next()
    await message.reply("Lavozimingizni kiriting:", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(bm))


@dp.message_handler(state=KForm.rank)
async def rank(message: Message, state: FSMContext):
    rank = message.text
    await state.update_data(rank=rank)
    await KForm.next()
    await message.reply("Login qoldiring \n  ⚠️(login va parolingizni unitib qoysangiz tiklash uchun RTTM bo'limiga uchrashishingiz kerak bo'ladi !) ", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(bm))


@dp.message_handler(state=KForm.login)
async def login(message: Message, state: FSMContext):
    login = message.text
    await state.update_data(login=login)
    await KForm.next()
    await message.reply("Parol qoldiring \n  ⚠️(login va parolingizni unitib qoysangiz tiklash uchun RTTM bo'limiga uchrashishingiz kerak bo'ladi !) ",reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(bm))


@dp.message_handler(state=KForm.parol)
async def tel(message: Message, state: FSMContext):
    parol = message.text
    user_data = await state.get_data()
    user_id = message.from_user.id
    createkerio(user_id, user_data['fullname'], user_data['department'], user_data['rank'], user_data['login'], parol)
    await state.finish()
    await message.reply("Ariza muvaffaqiyatli qabul qilindi!", reply_markup=button)


@dp.message_handler(lambda message: message.text == '📬 Elektron pochta xizmati 📬' and message.content_type == 'text')
async def checkout(message: types.Message):
    await message.answer("Xizmatni tanlang.\n Ariza yuborish. \n Arizani tekshirish", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).row(bm,bP,bP1))


@dp.message_handler(lambda message: message.text == '📬 Arizani tekshirish 📬' and message.content_type == 'text')
async def check(message: types.Message):
    user_id = message.from_user.id
    response = requests.get("http://127.0.0.1:8000/api/myv/pochta")
    data = response.json()
    a=0
    for i in data:
        if str(user_id) == i['user_id']:
            poch = i['pochta']
            parol= i['parol']
            a+=1
            await message.answer(f"Sizning pochtangiz: {poch} \nParolingiz: {parol} ")
    if a==0:
        await message.answer(f"Sizning pochtangiz topilmadi ")
    await send_welcome(message)

@dp.message_handler(lambda message: message.text == '📬 Elektron pochta ochish 📬' and message.content_type == 'text')
async def pochta(message: types.Message):
    await PForm.fullname.set()
    await message.answer("Assalomu alaykum! Ismingizni kiriting.", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(bm))


@dp.message_handler(lambda message: message.text == '🔙 Bosh menyuga qaytish', state="*")
async def back_to_start(message: Message, state: FSMContext):
    await state.finish()
    await send_welcome(message)


@dp.message_handler(state=PForm.fullname)
async def fullname(message: Message, state: FSMContext):
    user_name = message.text
    await state.update_data(fullname=user_name)
    await PForm.next()
    await message.reply("Bo'lim yoki kafedrangizni tanlang", reply_markup=button1)


@dp.message_handler(state=PForm.department)
async def department(message: Message, state: FSMContext):
    kafl = message.text
    await state.update_data(department=kafl)
    await PForm.next()
    await message.reply("Lavozimingizni kiriting:", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(bm))


@dp.message_handler(state=PForm.rank)
async def rank(message: Message, state: FSMContext):
    rank = message.text
    user_data = await state.get_data()
    user_id = message.from_user.id
    createpochta(user_id, user_data['fullname'], user_data['department'],  rank)
    await state.finish()
    await message.reply("Ariza muvaffaqiyatli qabul qilindi!", reply_markup=button)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)