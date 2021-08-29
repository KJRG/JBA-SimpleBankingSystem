word = input()
snake_case = ""
counter = 0
for char in word:
    if char.islower():
        snake_case += char
    else:
        if counter > 0:
            snake_case += "_"
        snake_case += char.lower()
    counter += 1
print(snake_case)
