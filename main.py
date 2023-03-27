def solution(my_string):
    answer = 0
    my_string = list(my_string)
    num = ""
    while my_string:
        e = my_string.pop()
        if e.isdigit():
            num += e
            if len(my_string) == 0:
                answer += int(num[::-1])
                break
        elif not e.isdigit() and len(num) > 0:
            answer += int(num[::-1])
            num = ""

    return answer


print(solution("10"))
