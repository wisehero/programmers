from collections import deque
def solution(food):
    foods = deque()

    for i in range(len(food) - 1, -1, -1):
        if i == 0:
            foods.insert(len(foods) // 2, 0)
        if food[i] % 2 == 0:
            while food[i] > 0:
                foods.appendleft(i)
                food[i] -= 1
                foods.append(i)
                food[i] -= 1
        else:
            while food[i] > 1:
                foods.appendleft(i)
                food[i] -= 1
                foods.append(i)
                food[i] -= 1
    answer = ''
    for s in foods:
        answer += str(s)
    return answer


food = [1, 7, 1, 2]
print(solution(food))
