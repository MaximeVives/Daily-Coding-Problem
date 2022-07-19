import itertools

input = [3, 2, 1]

all_perm = [list(t) for t in itertools.permutations(input)]
all_perm.sort()

print(all_perm)