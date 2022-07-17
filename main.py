import random

def random_access_memory(max, exceptions):
    valid_list = list(set([i for i in range(max)]) - set(exceptions)) 
    return random.choice(valid_list)


n = 6
l = [1, 3, 5]

print(random_access_memory(n, l))

