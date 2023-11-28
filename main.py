from itertools import combinations, permutations

n, m = map(int, input().split())
arr = [x for x in range(1, n + 1)]

for case in list(permutations(arr, m)):
    print(*case)
