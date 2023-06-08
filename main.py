import telebot
print('iniciando')
TOKEN = '6021346806:AAFMBfDMzplaQ7PVKr3SsqacxgGhhscJRKQ'
bot = telebot.TeleBot(TOKEN, threaded=False)

@bot.message_handler(func=lambda m:True)
def on_message(message):
    print('mensagem recebida')
    bot.reply_to(message, message.text)

def hello_http(event, context):
    print("evento")
    update = telebot.types.Update.de_json(event['body'])
    try:
        bot.process_new_updates([update])
    except:
        pass
    return {"statusCode": 200, "body": "hello world"}

from flask import Flask

app = Flask('')

@app.route('/')
def main():
    return "Your bot is alive!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
