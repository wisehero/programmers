from itertools import permutations
import sys

# n = 레일 개수
# m = 택배 바구니의 무게
# k = 일의 시행 횟수
n, m, k = map(int, sys.stdin.readline().split(" "))
input_rails = list(map(int, sys.stdin.readline().split(" ")))
result = 0

rails_case = permutations(input_rails, n)

for now_rails in rails_case:

    rails = list(now_rails)

    i = 0
    bucket = 0
    work = 0
    this_all = 0

    while work != k:
        if bucket + rails[i] <= m:
            bucket += rails[i]
            rails.append(rails[i])
            i += 1
        else:
            this_all += bucket
            bucket = 0
            work += 1

    if result == 0:
        result = this_all
    else:
        result = min(result, this_all)

print(result)
