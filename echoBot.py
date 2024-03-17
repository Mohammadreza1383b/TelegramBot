import telebot

bot = telebot.TeleBot("6906101229:AAGht13sGaxcrV7GqKozrcGXiaP2EtwGwY8")
first_button = telebot.types.InlineKeyboardButton("کلید اول" , url="https://t.me/drproxy_channel")
second_button = telebot.types.InlineKeyboardButton("کلید دوم" , url="https://t.me/drproxy_channel")
markup = telebot.types.InlineKeyboardMarkup()
markup.add(first_button , second_button)
@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.send_message(message.chat.id,"سلام به ربات ما خوش امدید" , reply_markup=markup)
    print(message)

@bot.message_handler(commands=['help'])
def help_function(message):
    bot.reply_to(message,"چه کمکی میتوانم بکنم؟")

bot.infinity_polling()