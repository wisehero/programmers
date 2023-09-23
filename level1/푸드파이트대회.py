# 먹는 음식의 종류와 양이 같다.
# 음식을 먹는 순서도 같다.
def solution(food):
    answer = "0"
    food = food[::-1]
    food.pop()

    m = len(food)

    for i in range(len(food)):
        for _ in range(food[i] // 2):
            answer = str(m) + answer + str(m)
        m -= 1

    return answer
