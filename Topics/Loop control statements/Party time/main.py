guests = list()
while True:
    user_input = input()
    if user_input == ".":
        break
    guests.append(user_input)
print(guests)
print(len(guests))
