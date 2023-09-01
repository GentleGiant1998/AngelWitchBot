import telebot


bot = telebot.TeleBot('6575657548:AAGKU2_1iFvEzqLsM43wlfjxBZv6_SQMN2o')


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Дарова!")


@bot.message_handler(func=lambda message: True)
def all_message(message):
    bot.reply_to(message, message.text)
   
    
bot.polling()