import itertools

inp = [3,2,1]

def findNextBigPerm(input):
    # find all permutation
    all_perm = list(itertools.permutations(input))
    # sort from lower to higher
    all_perm.sort()
    # transform each one to a number
    all_int = []
    for perm in all_perm:
        i = int(''.join(str(x) for x in perm))
        all_int.append(i)
    
    # find the initial number 
    init_number = all_int.index(int("".join(str(x) for x in input)))


    # if the initial number is the last in the list, get the first number
    # else get the next one in the list 
    next_one = all_int[(init_number + 1) % len(all_int)]
    # transform the number in a list
    return [int(x) for x in str(next_one)]

print(findNextBigPerm(inp))
