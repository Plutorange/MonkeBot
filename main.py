import telebot
import random

bot = telebot.TeleBot('6151807605:AAFRrkIsv5kNVFwVcUZ20VFvhDgBtjl1viA')
directory_images = ['monke_memes', 'monke_nft']
directory_monke_memes = [
    '1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpeg', '11jpeg'
]
directory_monke_nfts = [
    '1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.png', '7.png', '8.png', '9.jpg', '10.jpg', '11.jpg',
    '12.jpg', '13.jpg', '14.png'
]


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Добро пожаловать в нашу карточную игру MonkeyRush! Сделай свой ход - \n"
                                               "испытай удачу и получи карточку (/getcard)")
    elif message.text == '/description':
        bot.register_next_step_handler(message, description)
    elif message.text == '/getcard':
        bot.register_next_step_handler(message, getcard)

    else:
        bot.send_message(message.from_user.id, "Приветствуем, дружище! Выбери, что хочешь посмотреть: \n"
                                               "Используй /start , чтобы начать. \n"
                                               "Используй /description , чтобы посмотреть краткое, но понятное описание этого бота.")


# def help(message):
#     bot.send_message(message.from_user.id, '')

def getcard(message):
    choosen_directory = directory_images[random.randint(0, len(directory_images) - 1)]
    monke_memes = directory_images[0]
    monke_nfts = directory_images[1]
    card_path = ''
    if choosen_directory == monke_memes:
        card_path = (r'C:\Users\User\PycharmProjects\git_project\bot\monke_images\{}\{}'.format(monke_memes,
                                                                                                directory_monke_memes[
                                                                                                    random.randint(0,
                                                                                                                   len(directory_monke_memes) - 1)]))
    elif choosen_directory == monke_nfts:
        card_path = (r'C:\Users\User\PycharmProjects\git_project\bot\monke_images\{}\{}'.format(monke_nfts,
                                                                                                directory_monke_nfts[
                                                                                                    random.randint(0,
                                                                                                                   len(directory_monke_nfts) - 1)]))
    card = open(card_path, 'rb')
    bot.send_photo(message.chat.id, photo=card)
    bot.send_message('Держи свою карточку, приходи за следующей через 4 часа :)')


def description(message):
    bot.send_message(message.from_user.id,
                     'Коллекционные карточки и карточные игры появились задолго до NFT и остаются популярными еще с 90-х годов. '
                     'Собиратели тратят огромные суммы, чтобы заполучить в свою коллекцию редкий экземпляр, будь то карточка с покемоном или другим ценным героем. \n'
                     'Некоторые экземпляры настолько редки и уникальны, что становятся выгодными активами. \n'
                     'В нашем проекте имеется большое разнообразие карточек (категории: мемы, NFT и т.п.)за которые вам не придется платить, нужно будет лишь подождать некоторое время. \n'
                     'Также вы можете просматривать свою коллекцию и сравнивать её с другими.')


bot.polling(none_stop=True, interval=0)
