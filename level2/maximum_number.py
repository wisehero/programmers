from itertools import permutations


def solution(numbers):
    p = permutations(numbers, len(numbers))
    p_str = []
    for i in p:
        p_str.append("".join(list(map(str, i))))
    print(p_str)
    p_str = list(map(int, p_str))
    answer = max(p_str)
    print(str(answer))


numbers = [6, 10, 2]


def optimalSolution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))


print(optimalSolution(numbers))
