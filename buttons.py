from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import requests

# Barcha ma'lumotlarni chaqirish
response = requests.get("http://127.0.0.1:8000/api/myv/bolimlar/")
data = response.json()

# Boshlang'ich bo'sh ro'yxat
a = []

# Tugmalar uchun ReplyKeyboardMarkup yaratish
button = ReplyKeyboardMarkup(resize_keyboard=True)

# Birinchi va ikkinchi tugmalar qo'shish
b1 = KeyboardButton('🖥 Texnik xizmat ko`rsatish 🖥')
b2 = KeyboardButton('🌐 Wi-Fi uchun login/parol olish 🌐')
b3 = KeyboardButton('📬 Elektron pochta xizmati 📬')
bm = KeyboardButton('Asosiy menyuga qaytish')
button.add( b1, b2)
button.row(b3)



bm = KeyboardButton('🔙 Bosh menyuga qaytish')


# Boshqa tugmalar uchun ReplyKeyboardMarkup yaratish
button1 = ReplyKeyboardMarkup(resize_keyboard=True)
button1.add(bm)
# API dan olingan ma'lumotlar bo'yicha tugmalar yaratish
for i in data:
    j = type(i['id'])
    a.append(KeyboardButton(text=i['name'], callback_data=str(i['id'])))
    button1.add(a[-1])  # Olingan tugmani ReplyKeyboardMarkup ga qo'shish

bP = KeyboardButton('📬 Elektron pochta ochish 📬')
bP1 = KeyboardButton('📬 Arizani tekshirish 📬')
