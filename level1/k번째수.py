def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        a, b, c = commands[i]
        new_array = array[a - 1: b]
        new_array.sort()
        answer.append(new_array[c - 1])
    return answer
