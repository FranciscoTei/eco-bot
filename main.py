import telebot
from flask import Flask, request

TOKEN = '6021346806:AAFMBfDMzplaQ7PVKr3SsqacxgGhhscJRKQ'
bot = telebot.TeleBot(TOKEN, threaded = False)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Olá! Bem-vindo ao bot do Telegram.")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

app = Flask(__name__)

@app.route(f'/{TOKEN}', methods=['POST'])
def handle_webhook():
    update = telebot.types.Update.de_json(request.get_json(force=True))
    bot.process_new_updates([update])
    return "OK"

@app.route('/')
def main():
    return "Your bot is alive!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
