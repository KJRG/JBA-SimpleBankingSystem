# Write your code here

from account import create_account, is_card_number_valid
import database_manager


def add_new_account():
    global last_card_number
    account_id = last_card_number
    last_card_number += 1
    new_account = create_account(account_id)
    database_manager.insert_account(new_account)
    print("Your card has been created")
    print("Your card number:")
    print(new_account.card_number)
    print("Your card PIN:")
    print(new_account.pin)


def try_login_and_run_account_menu():
    input_card_number = input("Enter your card number:\n")
    input_pin = input("Enter your PIN:\n")
    print()
    user_account = database_manager.find_account_by_card_number(input_card_number)
    if (not user_account) or (user_account.pin != input_pin):
        print("Wrong card number or PIN!")
        return
    print("You have successfully logged in!")
    exit_from_submenu = run_account_menu(user_account)
    return exit_from_submenu


def run_account_menu(account):
    continue_running_account_menu = True
    exit_program = False
    while continue_running_account_menu:
        print("""
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit""")
        account_menu_user_input = input()
        print()
        if account_menu_user_input == "1":
            print_balance(account)
        elif account_menu_user_input == "2":
            add_income(account)
        elif account_menu_user_input == "3":
            transfer_money(account)
        elif account_menu_user_input == "4":
            close_account(account)
        elif account_menu_user_input == "5":
            print("You have successfully logged out!")
            continue_running_account_menu = False
        elif account_menu_user_input == "0":
            exit_program = True
            continue_running_account_menu = False
        else:
            print("Unknown input")
    return exit_program


def print_balance(account):
    print("Balance: {}".format(account.balance))


def add_income(account):
    print("Enter income:\n")
    income = int(input())
    account.balance += income
    database_manager.update_account(account)
    print("Income was added!")


def transfer_money(account):
    print("Transfer")
    print("Enter card number:")
    destination_card_number = input()
    if not is_card_number_valid(destination_card_number):
        print("Probably you made a mistake in the card number. Please try again!")
        return
    destination_account = database_manager.find_account_by_card_number(destination_card_number)
    if not destination_account:
        print("Such a card does not exist.")
        return
    print("Enter how much money you want to transfer:")
    amount_to_transfer = int(input())
    if amount_to_transfer > account.balance:
        print("Not enough money!")
        return
    account.balance -= amount_to_transfer
    destination_account.balance += amount_to_transfer
    database_manager.update_account(account)
    database_manager.update_account(destination_account)


def close_account(account):
    database_manager.delete_account(account)
    print("The account has been closed!")


database_manager.init_db()
last_card_number = database_manager.get_accounts_count()
continue_running = True
while continue_running:
    print("""
1. Create an account
2. Log into account
0. Exit""")
    user_input = input()
    print()
    if user_input == "1":
        add_new_account()
    elif user_input == "2":
        exit_after_submenu = try_login_and_run_account_menu()
        if exit_after_submenu:
            continue_running = False
    elif user_input == "0":
        continue_running = False
    else:
        print("Unknown input")

database_manager.close()
print("Bye!")
