min_hours_of_sleep = int(input())
max_hours_of_sleep = int(input())
user_hours_of_sleep = int(input())

if user_hours_of_sleep < min_hours_of_sleep:
    print("Deficiency")
else:
    if user_hours_of_sleep > max_hours_of_sleep:
        print("Excess")
    else:
        print("Normal")
