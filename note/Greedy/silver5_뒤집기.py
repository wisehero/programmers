s = input()
one = 0
zero = 0
c = s[0]
for i in s:
    if i != c and c == "1":
        one += 1
        c = "0"
    if i != c and c == "0":
        zero += 1
        c = "1"

if c == "1":
    one += 1
else:
    zero += 1
print(min(one, zero))
