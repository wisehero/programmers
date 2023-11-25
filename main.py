n, m = map(int, input().split())

i = 1
name_num = {}
num_name = {}

for _ in range(n):
    a = input()
    name_num[a] = i
    num_name[i] = a
    i += 1

for _ in range(m):
    a = input()
    if a.isdigit():
        print(num_name[int(a)])
    else:
        print(name_num[a])
