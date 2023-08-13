n = int(input())

cards = [x for x in range(n, 0, -1)]
left_card = []

flag = True
while len(cards) != 1:
    if flag:
        left_card.append(cards.pop())
        flag = False
    else:
        cards = [cards.pop()] + cards
        flag = True

for i in left_card:
    print(i, end=' ')
print(cards[0])
