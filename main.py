import os
import telebot


categories = [
    '🍟 Продукты(еда, продукты, food)',
    '🍽 Обед(столовая, ланч, dinner)',
    '🚌 Проезд(автобус, трамвай, такси, transport)',
    '🌐 Интернет(internet, инет)',
    '🏦 Банк(сбер, bank)',
    '📱 Телефон(мтс, связь, phone)',
    '🗑 Прочее(other)'
]

API_TOKEN = os.environ.get('API_TOKEN') or '1346588563:AAF_oQ-fzmC2IfdcMWYL-2p_Hc3SYt1-BE8'
ADMIN_ID = 746354179
bot = telebot.TeleBot(API_TOKEN, parse_mode=None)


def auth(func):
    '''Аутентификация'''
    def wrapper(message):
        if message.from_user.id != ADMIN_ID:
            return bot.send_message(message.chat.id, 'Acces Denied')
        return func(message)
    return wrapper


@bot.message_handler(commands=['start'])
@auth
def start(message):
    '''Старт работы с ботом'''
    text_message = f'Добро пожаловать, {message.from_user.first_name}👋\
                    \nЯ помогу тебе стать экономным🤑\
                    \nУзнай функционал бота, тыкнув на комманду 👉 /help'
    bot.send_message(message.chat.id, text_message)


@bot.message_handler(commands=['add_expense'])
@auth
def add_expense(message):
    '''Добавить трату'''
    pass


@bot.message_handler(commands=['categories'])
@auth
def send_categories(message):
    '''Высылает все категории трат'''
    text_message = f'📂 Категории расходов:'
    for category in categories:
        text_message += f'\n\n{category}'
    bot.send_message(message.chat.id, text_message)


@bot.message_handler(commands=['add_category'])
@auth
def add_category(message):
    '''Добавление категории в базу'''
    category = message.text.replace('/add_category', '')[1:]
    if category:
        categories.insert(-1, category)
        bot.send_message(message.chat.id, 
                        f'👍 Категория \'{category}\' добавлена в ваш список')
        return None
    bot.send_message(message.chat.id, f'⚠️ Категория не добавлена')


@bot.message_handler(commands=['del_category'])
@auth
def del_category(message):
    '''Удаление категории из базы'''
    category = message.text.replace('/del_category ', '')
    if category in categories:
        categories.remove(category)
        bot.send_message(message.chat.id, 
                        f'❌ Категория \'{category}\' удалена!')
        return None
    bot.send_message(message.chat.id, f'🔍 Категория не найдена')


@bot.message_handler(commands=['help'])
@auth
def all_commnads(message):
    '''Высылает список комманд бота'''
    bot.send_message(message.chat.id,
                    f'⚒ Функционал:\
                        \n\n/start - Приветствие 👋\
                        \n\n/categories - Список категорий трат 📖\
                        \n\n/add_category - Добавить категорию ✅\
                        \n\n/del_category - Удалить категорию ❌'
    )


@bot.message_handler(content_types=['sticker'])
@auth
def send_info(message):
    print(message)


@bot.message_handler(content_types=['text'])
@auth
def send_text(message):
    if message.text.lower() in ['привет', 'здарова', 'ку']:
        sticker_id = 'CAACAgIAAxkBAAMiX5Q6iuDcIbCHVpHRBjgpW7xq8NIAAgEAA5KfHhEKX1MC7Bfm9hsE'
        bot.send_sticker(message.chat.id, sticker_id)


@bot.message_handler(content_types=['video', 'document', 'audio', 'sticker'])
@auth
def send_universal_response(message):
    bot.send_message(message.chat.id, 'Ничего не понял, но очень интересно!')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAOCX5UvkoequxNz4sv_VK4ngTbsbsoAAl8AA5KfHhEKnPzK-5zndBsE')


if __name__ == "__main__":
    bot.polling()