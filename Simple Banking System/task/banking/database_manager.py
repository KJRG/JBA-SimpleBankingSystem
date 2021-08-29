import sqlite3
from account import Account

con = sqlite3.connect('card.s3db')


def init_db():
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS card (
    id INTEGER,
    number TEXT,
    pin TEXT,
    balance INTEGER DEFAULT 0
);''')
    con.commit()


def get_accounts_count():
    cur = con.cursor()
    cur.execute('SELECT COUNT(*) FROM card')
    row = cur.fetchone()
    return row[0]


def find_account_by_card_number(card_number):
    cur = con.cursor()
    cur.execute(f'SELECT * FROM card WHERE number = {card_number}')
    row = cur.fetchone()
    if not row:
        return None
    account_from_db = Account(row[0], row[1], row[2], row[3])
    return account_from_db


def insert_account(new_account):
    cur = con.cursor()
    query = f'''INSERT INTO card (id, number, pin, balance)
VALUES ({new_account.account_id}, {new_account.card_number}, {new_account.pin}, {new_account.balance})'''
    cur.execute(query)
    con.commit()


def update_account(account_to_update):
    cur = con.cursor()
    cur.execute(f'''UPDATE card SET
number = {account_to_update.card_number},
pin = {account_to_update.pin},
balance = {account_to_update.balance}
WHERE id = {account_to_update.account_id}''')
    con.commit()


def delete_account(account_to_delete):
    cur = con.cursor()
    cur.execute(f'DELETE FROM card WHERE id = {account_to_delete.account_id}')
    con.commit()


def close():
    con.close()
