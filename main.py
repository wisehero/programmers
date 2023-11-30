n = input()

arr = []

for i in range(len(n)):
    arr.append(n[i:])

for a in sorted(arr):
    print(a)

