from collections import Counter

word = input()
word = word.upper()
c = Counter(word)
c = list(c.items())
c.sort(key=lambda x: -x[1])

if len(c) >= 2 and c[0][1] == c[1][1]:
    print("?")
else:
    print(c[0][0].upper())
