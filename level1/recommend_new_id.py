def solution(new_id):
    answer = ''
    al = "abcdefghijklmnopqrstuvwxyz"
    ch = "-_."
    numbers = "0123456789"

    # 1단계
    first = new_id.lower()
    second = ''
    # 2단계
    for i in range(len(first)):
        if first[i] in al or first[i] in ch or first[i] in numbers:
            second += first[i]

    second = list(second)

    # 3단계
    third = ''
    print(answer)
    for i in range(len(second)):
        if i + 1 == len(second):
            third += second[i]
            break
        if second[i] == "." and second[i + 1] == ".":
            continue
        third += second[i]

    third = list(third)
    print(third)

    # 4단계
    if len(third) != 0:
        if third[0] == ".":
            third.pop(0)

        if len(third) != 0 and third[-1] == ".":
            third.pop()

    # 5단계
    if len(third) == 0:
        third = "a"
    # 6단계
    if len(third) >= 16:
        third = third[0:15]
        if third[-1] == ".":
            third.pop()

    # 7단계
    if len(third) <= 2:
        while True:
            if len(third) == 3:
                break;
            third += third[-1]

    answer = "".join(third)
    print(answer)
    return answer


def optimalSolution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer
