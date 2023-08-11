n, m = map(int, input().split(" "))

a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))

a = set(a)
b = set(b)
a_b = a - b
b_a = b - a
print(len(a_b.union(b_a)))
