income = int(input())
percent = 0
if income <= 15527:
    percent = 0
elif 15528 <= income <= 42707:
    percent = 15
elif 42708 <= income <= 132406:
    percent = 25
else:
    percent = 28
calculated_tax = round(income * percent / 100)
info = f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!'
print(info)
