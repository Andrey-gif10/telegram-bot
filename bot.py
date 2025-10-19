import telebot, random
from config import TOKEN
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=["start"])
def hi(message):
    bot.reply_to(message,"hello user")
    bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAETDuZo6-Y3QJ1GukhU6BGllAqt7n6zfAACmEMAAqGZcEuC7NRcrtUofjYE")
@bot.message_handler(commands=["about_bot"])
def news(message):
    bot.reply_to(message,"test bot for programming")
    bot.send_message(message.chat.id,"test command") 

@bot.message_handler(commands=["password_create"])  
def alfavit(message):
    alfabet = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"  


    n = int(message.text.split()[1]) 
    
    
    password = ""
    for i in range(n):
        password += random.choice(alfabet)
    bot.reply_to(message,"your password: " + password)      
bot.polling()