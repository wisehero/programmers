cash = int(input())

n = int(input())
for _ in range(n):
    a, b = map(int, input().split(" "))
    cash -= a * b

if cash == 0:
    print("Yes")
else:
    print("No")
