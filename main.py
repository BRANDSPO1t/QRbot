import qrcode
import telebot

bot = telebot.TeleBot('<bot_token>')

@bot.message_handler(commands = ['start'])
def main(message):
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.last_name} {message.from_user.first_name}! Этот бот конвертирует информацию в QRcode!')
    bot.send_message(message.chat.id, 'Напиши текст, кторый хочешь конвертировать в QRcode')
    bot.register_next_step_handler(message, qr)

def qr(message):
    data = message.text
    img = qrcode.make(data)
    type(img)
    img.save('qrfile.png')
    fileop = open('qrfile.png', 'rb')
    bot.send_photo(message.chat.id, fileop)

bot.polling(none_stop = True)



























