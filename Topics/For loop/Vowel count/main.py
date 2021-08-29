string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
vowel_count = 0
for char in string:
    if char in vowels:
        vowel_count += 1
print(vowel_count)
