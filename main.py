from itertools import permutations

n = int(input())
arr = list(range(1, n + 1))

for case in list(permutations(arr, n)):
    print(*case)
