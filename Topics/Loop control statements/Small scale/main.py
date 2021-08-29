input_numbers = list()
while True:
    user_input = input()
    if user_input == ".":
        break
    input_numbers.append(float(user_input))
print(min(input_numbers))
