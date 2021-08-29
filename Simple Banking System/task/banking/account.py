from random import choice
from string import digits


PIN_LENGTH = 4
ACCOUNT_ID_LENGTH = 9
IIN = "400000"


class Account:
    def __init__(self, account_id, card_number, pin, balance):
        self.account_id = account_id
        self.card_number = card_number
        self.pin = pin
        self.balance = balance


def create_account(account_id):
    card_number = create_card_number(account_id)
    pin = create_pin()
    new_account = Account(account_id, card_number, pin, 0)
    return new_account


def create_card_number(account_id):
    account_id_str = str(account_id).zfill(ACCOUNT_ID_LENGTH)
    card_number_without_checksum = IIN + account_id_str
    checksum = get_card_number_checksum(card_number_without_checksum)
    return card_number_without_checksum + checksum


def get_card_number_checksum(card_number):
    luhn_total_sum = 0
    i = 1
    for char in card_number:
        x = int(char)
        if i % 2 != 0:
            x *= 2
        if x > 9:
            x -= 9
        luhn_total_sum += x
        i += 1
    luhn_checksum = (10 - (luhn_total_sum % 10)) % 10
    return str(luhn_checksum)


def create_pin():
    pin = ""
    for i in range(0, PIN_LENGTH):
        pin += choice(digits)
    return pin


def is_card_number_valid(card_number):
    card_number_without_checksum = card_number[:-1]
    card_number_checksum = card_number[-1]
    correct_checksum = get_card_number_checksum(card_number_without_checksum)
    return card_number_checksum == correct_checksum
