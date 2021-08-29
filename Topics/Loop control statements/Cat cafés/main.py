names = list()
kittens_counts = list()
index = 0
count_to_index_map = dict()
while True:
    user_input = input()
    if user_input == "MEOW":
        break
    input_data = user_input.split()
    name = input_data[0]
    count = int(input_data[1])
    names.append(name)
    kittens_counts.append(count)
    count_to_index_map[count] = index
    index += 1
max_count = max(kittens_counts)
name_index = count_to_index_map[max_count]
print(names[name_index])
