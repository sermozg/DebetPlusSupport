import constants
import telebot


bot = telebot.TeleBot(constants.TOKEN_TG)


@bot.message_handler(content_types=['text'])
def repeat_all_message(message):

    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
