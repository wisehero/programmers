def solution(topping):
    answer = 0
    foward = set()
    backward = {}
    for i in topping:
        backward[i] = backward.get(i, 0)
        backward[i] += 1

    for i in topping:
        foward.add(i)
        backward[i] -= 1

        if backward[i] == 0:
            del backward[i]
        if len(foward) == len(backward.keys()):
            answer += 1
    return answer
