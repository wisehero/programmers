n = int(input())
cards = list(range(1, n + 1))
ans = []
while cards:
    ans.append(cards.pop(0))
    if not cards:
        break
    cards.append(cards.pop(0))

print(*ans)
