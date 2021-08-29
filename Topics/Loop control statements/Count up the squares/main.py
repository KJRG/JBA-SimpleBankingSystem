# put your python code here
sum_of_numbers = 0
sum_of_squares = 0
while True:
    number = int(input())
    sum_of_numbers += number
    sum_of_squares += (number ** 2)
    if sum_of_numbers == 0:
        break
print(sum_of_squares)
