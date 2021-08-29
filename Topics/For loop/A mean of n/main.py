n = int(input())
sum_of_input = 0
for _ in range(n):
    sum_of_input += int(input())
mean = 0.0
if n > 0:
    mean = sum_of_input / n
print(mean)
