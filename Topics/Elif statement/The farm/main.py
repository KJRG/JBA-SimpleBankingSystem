money = int(input())

animal = ""
animal_value = 0

if money < 23:
    animal = "None"
elif money < 678:
    animal = "chicken"
    animal_value = 23
elif money < 1296:
    animal = "goat"
    animal_value = 678
elif money < 3848:
    animal = "pig"
    animal_value = 1296
elif money < 6769:
    animal = "cow"
    animal_value = 3848
else:
    animal = "sheep"
    animal_value = 6769

if animal != "None":
    number_of_animals = money // animal_value
    if animal != "sheep" and number_of_animals > 1:
        animal += "s"
    print(number_of_animals, animal)
else:
    print(animal)
