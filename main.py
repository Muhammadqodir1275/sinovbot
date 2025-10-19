import telebot
import os

from dotenv import load_dotenv  # .env faylni o‘qish uchun

# .env fayldan o‘zgaruvchilarni yuklash
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# /start komandasi
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user = message.from_user.first_name  # foydalanuvchi ismi
    text = f"👋 Salom, {user}!\n\n🤖 Men sizning yordamchingizman!\n\n"
    text += "Quyidagi menyulardan birini tanlang 👇"

    # Tugmalar
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("ℹ️ Ma'lumot")
    btn2 = telebot.types.KeyboardButton("🕹 Funksiya")
    btn3 = telebot.types.KeyboardButton("💬 Aloqa")
    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, text, reply_markup=markup)

# Oddiy matnli xabarlar uchun
@bot.message_handler(func=lambda message: True)
def menu_handler(message):
    if message.text == "ℹ️ Ma'lumot":
        bot.reply_to(message, "Bu bot test loyihasi. Siz undan turli funksiya o‘rganishingiz mumkin 😊")
    elif message.text == "🕹 Funksiya":
        bot.reply_to(message, "Hozircha bu bo‘limda yangi funksiyalar sinovda 👨‍💻")
    elif message.text == "💬 Aloqa":
        bot.reply_to(message, "Admin bilan aloqa: @YourUsername")
    else:
        bot.reply_to(message, "Iltimos, menyudagi tugmalardan birini tanlang 👇")

# Botni ishga tushurish
print("🤖 Bot ishga tushdi...")
bot.polling(non_stop=True)
