text = input()
vowels = ["a", "e", "i", "o", "u"]
for char in text:
    if char.isalpha():
        if char in vowels:
            print("vowel")
        else:
            print("consonant")
    else:
        break
