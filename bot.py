import telebot

TOKEN = '6021346806:AAFMBfDMzplaQ7PVKr3SsqacxgGhhscJRKQ'
bot = telebot.TeleBot(TOKEN, threaded=False)

@bot.message_handler(func=lambda m:True)
def on_message(message):
    bot.reply_to(message, message.text)

def hello_http(event, context):
    update = telebot.types.Update.de_json(event['body'])
    try:
        bot.process_new_updates([update])
    except:
        pass
    return {"statusCode": 200, "body": "hello world"}