import random

# your sentence is assigned to the variable
sentence = input().split()

# write your python code below
SEED = 43
random.seed(SEED)
random.shuffle(sentence)

# shows the message
print(' '.join(sentence))
