import threading
import time
import telebot
from telebot import types
import random

bot = telebot.TeleBot('6151807605:AAFRrkIsv5kNVFwVcUZ20VFvhDgBtjl1viA')
directory_images = ['monke_memes', 'monke_nft', 'monke_mini', 'monke_cartoons', 'monke_games']
directory_monke_memes = [
    '1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpeg',
    '11.jpeg'
]
directory_monke_nfts = [
    '1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.png', '7.png', '8.png', '9.jpg', '10.jpg',
    '11.jpg',
    '12.jpg', '13.jpg', '14.png'
]
directory_monke_mini = [
    '1.jpg', '2.jpeg', '3.jpeg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg'
]
directory_monke_cartoons = [
    '1.jpg', '2.jpg', '3.png', '4.jpg', '5.jpeg', '6.jpg', '7.jpg', '8.jpg', '9.png', '10.jpg'
]
directory_monke_games = [
    '1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg'
]
cards_bank = []
monkey_coins = 0
tim = time.time()


def timer(st, chat):
    global tim
    tim = st
    while True:
        t = time.time()
        if st + 15 <= t:
            bot.send_message(chat, '4 часа прошло')
            return


thread1 = threading.Thread(target=timer, args=(time.time(),), daemon=True)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/getcard")
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     "🙈Добро пожаловать в нашу карточную игру 💵MonkeyRush💵! Сделай свой ход - \n"
                     "испытай удачу и получи карточку (/getcard)🙈", reply_markup=markup)


@bot.message_handler(commands=['getcard'])
def getcard(message):
    global thread1
    global tim
    if thread1.is_alive():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b = int(time.time() - tim)
        h, m, s = b // 3600, b // 60 % 60, 15 - b % 60
        bot.send_message(message.from_user.id,
                         'К сожалению 4 часа еще не прошло\n'
                         f'приходи через {h}-{m}-{s}',
                         reply_markup=markup)
    else:
        global monkey_coins
        flag_nft = False
        flag_memes = False
        flag_cartoons = False
        flag_mini = False
        flag_games = False
        choosen_directory = directory_images[random.randint(0, len(directory_images) - 1)]
        monke_memes = directory_images[0]
        monke_nfts = directory_images[1]
        monke_mini = directory_images[2]
        monke_cartoons = directory_images[3]
        monke_games = directory_images[4]
        card_path = ''

        if choosen_directory == monke_memes:
            monkey_coins += 500

            flag_memes = True
            card_path = (
                r'monke_images/{}/{}'.format(
                    monke_memes,
                    directory_monke_memes[
                        random.randint(
                            0,
                            len(
                                directory_monke_memes) - 1)]))
        elif choosen_directory == monke_nfts:
            flag_nft = True
            monkey_coins += 1000
            card_path = (
                r'monke_images/{}/{}'.format(
                    monke_nfts,
                    directory_monke_nfts[
                        random.randint(
                            0,
                            len(
                                directory_monke_nfts) - 1)]))
        elif choosen_directory == monke_mini:
            flag_mini = True
            monkey_coins += 250
            card_path = (
                r'monke_images/{}/{}'.format(
                    monke_mini,
                    directory_monke_mini[
                        random.randint(
                            0,
                            len(
                                directory_monke_mini) - 1)]))
        elif choosen_directory == monke_cartoons:
            flag_cartoons = True
            monkey_coins += 750
            card_path = (
                r'monke_images/{}/{}'.format(
                    monke_cartoons,
                    directory_monke_cartoons[
                        random.randint(
                            0,
                            len(
                                directory_monke_cartoons) - 1)]))
        elif choosen_directory == monke_games:
            flag_games = True
            monkey_coins += 1500
            card_path = (
                r'monke_images/{}/{}'.format(
                    monke_games,
                    directory_monke_games[
                        random.randint(
                            0,
                            len(
                                directory_monke_games) - 1)]))

        card = open(card_path, 'rb')
        if flag_nft:
            if card_path in cards_bank:
                bot.send_photo(message.chat.id, photo=card)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton('/back2menu')
                markup.add(btn1)
                bot.send_message(message.from_user.id,
                                 '🙈К сожалению, такая карточка у тебя уже есть, приходи за следующей через 4 часа :) \n'
                                 '💰Всего: {} MC(+1000🪙 MonkeyCoins)🙈'.format(monkey_coins),
                                 reply_markup=markup)
            else:
                bot.send_photo(message.chat.id, photo=card)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton('/back2menu')
                markup.add(btn1)
                bot.send_message(message.from_user.id,
                                 '🙈Держи свою карточку, приходи за следующей через 4 часа :) \n'
                                 '💰Всего: {} MC(+1000🪙 MonkeyCoins)🙈'.format(monkey_coins),
                                 reply_markup=markup)
                cards_bank.append(card_path)
        elif flag_memes:
            if card_path in cards_bank:
                bot.send_photo(message.chat.id, photo=card)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton('/back2menu')
                markup.add(btn1)
                bot.send_message(message.from_user.id,
                                 '🙈К сожалению, такая карточка у тебя уже есть, приходи за следующей через 4 часа :) \n'
                                 '💰Всего: {} MC(+500🪙 MonkeyCoins)🙈'.format(monkey_coins),
                                 reply_markup=markup)
            else:
                bot.send_photo(message.chat.id, photo=card)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton('/back2menu')
                markup.add(btn1)
                bot.send_message(message.from_user.id,
                                 '🙈Держи свою карточку, приходи за следующей через 4 часа :) \n'
                                 '💰Всего: {} MC(+500🪙 MonkeyCoins)🙈'.format(monkey_coins),
                                 reply_markup=markup)
                cards_bank.append(card_path)
        elif flag_mini:
            if card_path in cards_bank:
                bot.send_photo(message.chat.id, photo=card)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton('/back2menu')
                markup.add(btn1)
                bot.send_message(message.from_user.id,
                                 '🙈К сожалению, такая карточка у тебя уже есть, приходи за следующей через 4 часа :) \n'
                                 '💰Всего: {} MC(+250🪙 MonkeyCoins)🙈'.format(monkey_coins),
                                 reply_markup=markup)
            else:
                bot.send_photo(message.chat.id, photo=card)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton('/back2menu')
                markup.add(btn1)
                bot.send_message(message.from_user.id,
                                 '🙈Держи свою карточку, приходи за следующей через 4 часа :) \n'
                                 '💰Всего: {} MC(+250🪙 MonkeyCoins)🙈'.format(monkey_coins),
                                 reply_markup=markup)
                cards_bank.append(card_path)
        elif flag_cartoons:
            if card_path in cards_bank:
                bot.send_photo(message.chat.id, photo=card)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton('/back2menu')
                markup.add(btn1)
                bot.send_message(message.from_user.id,
                                 '🙈К сожалению, такая карточка у тебя уже есть, приходи за следующей через 4 часа :) \n'
                                 '💰Всего: {} MC(+750🪙 MonkeyCoins)🙈'.format(monkey_coins),
                                 reply_markup=markup)
            else:
                bot.send_photo(message.chat.id, photo=card)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton('/back2menu')
                markup.add(btn1)
                bot.send_message(message.from_user.id,
                                 '🙈Держи свою карточку, приходи за следующей через 4 часа :) \n'
                                 '💰Всего: {} MC(+750🪙 MonkeyCoins)🙈'.format(monkey_coins),
                                 reply_markup=markup)
                cards_bank.append(card_path)
        elif flag_games:
            if card_path in cards_bank:
                bot.send_photo(message.chat.id, photo=card)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton('/back2menu')
                markup.add(btn1)
                bot.send_message(message.from_user.id,
                                 '🙈К сожалению, такая карточка у тебя уже есть, приходи за следующей через 4 часа :) \n'
                                 '💰Всего: {} MC(+1500🪙 MonkeyCoins)🙈'.format(monkey_coins),
                                 reply_markup=markup)
            else:
                bot.send_photo(message.chat.id, photo=card)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton('/back2menu')
                markup.add(btn1)
                bot.send_message(message.from_user.id,
                                 '🙈Держи свою карточку, приходи за следующей через 4 часа :) \n'
                                 '💰Всего: {} MC(+1500🪙 MonkeyCoins)🙈'.format(monkey_coins),
                                 reply_markup=markup)
                cards_bank.append(card_path)
        thread1 = threading.Thread(target=timer, args=(time.time(), message.chat.id), daemon=True)
        thread1.start()


@bot.message_handler(commands=['back2menu'])
def back2menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/minigames')
    btn2 = types.KeyboardButton('/cardsbank')
    btn3 = types.KeyboardButton('/getcard')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id,
                     '🙈Вы вернулись в главное меню! 👋Предлагаю тебе скрасить время ожидания: \n'
                     '📌можешь поиграть в кое-какие интересные мини игры; \n'
                     '📌можешь взглянуть на банк своих карточек; \n'
                     '📌а если время уже прошло, тогда вперед за новыми карточками!🙈',
                     reply_markup=markup)


@bot.message_handler(commands=['cardsbank'])
def cardsbank(message):
    global cards_bank
    counter_of_card = 1
    card_num = 0
    for card in cards_bank:
        for category in directory_images:
            if category in card:
                if card[-6] in '0123456789' and card[-7] in '0123456789':
                    card_num = card[-7] + card[-6]
                elif card[-5] in '0123456789' and card[-6] in '0123456789':
                    card_num = card[-6] + card[-5]
                elif card[-5] in '0123456789':
                    card_num = card[-5]
                bot.send_message(message.from_user.id,
                                 '{}. {}#{}'.format(counter_of_card, category.upper(),
                                                    int(card_num)))
                counter_of_card += 1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/back2menu')
    markup.add(btn1)
    bot.send_message(message.from_user.id, '🙈Кажется, это все... Вперед за новыми трофеями!🏆',
                     reply_markup=markup)


@bot.message_handler(commands=['minigames'])
def minigames(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/basketball')
    btn2 = types.KeyboardButton('/dice')
    btn3 = types.KeyboardButton('/football')
    btn4 = types.KeyboardButton('/jackpot')
    btn5 = types.KeyboardButton('/back2menu')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.from_user.id, '🙈Во что поиграем? Смотри какой богатый выбор...▶',
                     reply_markup=markup)


@bot.message_handler(commands=['basketball'])
def basketball(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/minigames')
    markup.add(btn1)
    bot.send_dice(message.from_user.id, '🏀')
    bot.send_message(message.from_user.id, '🙈Майкл Джордан тоже долго шел к своей заветной цели⛹‍♂!',
                     reply_markup=markup)


@bot.message_handler(commands=['dice'])
def dice(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/minigames')
    markup.add(btn1)
    bot.send_dice(message.from_user.id, '🎲')
    bot.send_message(message.from_user.id, '🙈Не останавливайся, пока не выбьешь 7!💅',
                     reply_markup=markup)


@bot.message_handler(commands=['football'])
def football(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/minigames')
    markup.add(btn1)
    bot.send_dice(message.from_user.id, '⚽')
    bot.send_message(message.from_user.id, '🙈Этот удар мне напомнил ЧМ-2⚽18!', reply_markup=markup)


@bot.message_handler(commands=['jackpot'])
def jackpot(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/minigames')
    markup.add(btn1)
    bot.send_dice(message.from_user.id, '🎰')
    bot.send_message(message.from_user.id,
                     '🙈А..Ази..Азино..Три топора? А это как тут вообще оказалось?🪓🪓🪓',
                     reply_markup=markup)


@bot.message_handler(commands=['description'])
def description(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/start')
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     '🙈Коллекционные карточки и карточные игры появились задолго до NFT и остаются популярными еще с 90-х годов. '
                     '📍Собиратели тратят огромные суммы, чтобы заполучить в свою коллекцию редкий экземпляр, будь то карточка с покемоном или другим ценным героем. \n'
                     '📍Некоторые экземпляры настолько редки и уникальны, что становятся выгодными активами. \n'
                     '📍В нашем проекте имеется большое разнообразие карточек (категории: мемы, NFT и т.п.)за которые вам не придется платить, нужно будет лишь подождать некоторое время. \n'
                     '📍Также вы можете просматривать свою коллекцию и сравнивать её с другими. Поехали!🙈',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def hello(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/start')
    btn2 = types.KeyboardButton('/description')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id,
                     "🙈Приветствуем, дружище! 👀Выбери, что хочешь посмотреть: \n"
                     "🧷Используй /start , чтобы начать. \n"
                     "🧷Используй /description , чтобы посмотреть краткое, но понятное описание этого бота.🙈",
                     reply_markup=markup)


bot.polling(none_stop=True, interval=0)
