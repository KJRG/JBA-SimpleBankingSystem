n = int(input())
numbers_divisible_by_7 = list()

for _ in range(0, n):
    input_number = int(input())
    if input_number % 7 == 0:
        numbers_divisible_by_7.append(input_number)

for number in numbers_divisible_by_7:
    print(str(number ** 2))
