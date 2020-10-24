import os
import telebot


API_TOKEN = os.environ.get('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN, parse_mode=None)


def auth(func):
    '''Аутентификация'''
    admin_id = 746354179
    def wrapper(message):
        if message.from_user.id != admin_id:
            return bot.send_message(message.chat.id, 'Acces Denied')
        return func(message)
    return wrapper


@bot.message_handler(commands=['start'])
@auth
def send_response(message):
    '''Старт работы с ботом'''
    text_message = f'Добро пожаловать, {message.from_user.username}👋\
                    \nЯ помогу тебе стать экономным🤑\
                    \nЯ создал несколько категорий расходов, тыкни на комманду 👉 /categories'
    bot.send_message(message.chat.id, text_message)


@bot.message_handler(commands=['categories'])
@auth
def send_categories(message):
    text_message = f'📂 Категории расходов:\
        \n\n🍟 продукты(еда, продукты, food)\
        \n\n🍽 обед(столовая, ланч, dinner)\
        \n\n🚌 проезд(автобус, трамвай, такси, transport)\
        \n\n🌐 интернет(internet, инет)\
        \n\n🏦 банк(сбер, bank)\
        \n\n📱 телефон(мтс, связь, phone)\
        \n\n🗑 прочее(other)'
    bot.send_message(message.chat.id, text_message)    


@bot.message_handler(commands=['help'])
@auth
def send_help_info(message):
    # Написать справочник комманд
    pass


@bot.message_handler(content_types=['text'])
@auth
def send_text(message):
    if message.text.lower() in ['привет', 'здарова', 'ку']:
        sticker_id = 'CAACAgIAAxkBAAMiX5Q6iuDcIbCHVpHRBjgpW7xq8NIAAgEAA5KfHhEKX1MC7Bfm9hsE'
        bot.send_sticker(message.chat.id, sticker_id)



if __name__ == "__main__":
    bot.polling()