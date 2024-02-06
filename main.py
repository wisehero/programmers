n, m = map(int, input().split())

s1 = set(input().split())
s2 = set(input().split())

print(len(s1.difference(s2)) + len(s2.difference(s1)))
