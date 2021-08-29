scores = input().split()
# put your python code here
total_score = 0
lives = 3
for user_answer in scores:
    if user_answer == "C":
        total_score += 1
    elif user_answer == "I":
        lives -= 1
        if lives <= 0:
            break
print("You won" if lives > 0 else "Game over")
print(total_score)
