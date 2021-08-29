# put your python code here
a = int(input())
b = int(input())
numbers_sum = 0
numbers_count = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        numbers_sum += i
        numbers_count += 1
mean = numbers_sum / numbers_count
print(mean)
