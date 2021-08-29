sum_of_input_numbers = 0
input_numbers_count = 0
while True:
    user_input = input()
    if user_input == ".":
        break
    sum_of_input_numbers += int(user_input)
    input_numbers_count += 1
mean = sum_of_input_numbers / input_numbers_count
print(mean)
