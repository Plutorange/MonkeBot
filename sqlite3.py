import sqlite3

_connection = None


def get_connection():
    global _connection
    if _connection is None:
        _connection = sqlite3.connect('telegram_bot.db')
    return _connection


def init_db(force: bool = False):
    conn = sqlite3.connect('telegram_bot.db', check_same_thread=False)

    c = conn.cursor()
    if force:
        c.execute('DROP TABLE IF EXISTS user_message')

    c.execute('''
        CREATE TABLE IF NOT EXISTS user_message (
            id          INTEGER PRIMARY KEY,
            user_id     INTEGER NOT NULL,
            coins       INTEGER NOT NULL
        )
    ''')
    conn.commit()


def add_coins(user_id: int, coins: int):
    conn = sqlite3.connect('telegram_bot.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('INSERT INTO user_message (user_id, coins) VALUES (?, ?)', (user_id, coins))
    conn.commit()


def get_coins(user_id: int):
    conn = sqlite3.connect('telegram_bot.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('SELECT FROM user_message WHERE user_id = ? LIMIT 1', (user_id,))
    res = c.fetchall()
    return res


def add_cards(user_id: int, cards: str):
    conn = sqlite3.connect('telegram_bot.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('INSERT INTO user_message (user_id, coins) VALUES (?, ?)', (user_id, cards))
    conn.commit()


def get_cards(user_id: int):
    conn = sqlite3.connect('telegram_bot.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('SELECT FROM user_message WHERE user_id = ? LIMIT 1', (user_id,))
    res = c.fetchall()
    return res


if __name__ == '__main__':
    init_db(force=True)
    add_coins(user_id=1234, coins=500)
