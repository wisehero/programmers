def solution(my_string):
    answer = []
    my_string = list(my_string)
    while my_string:
        c = my_string.pop(0)
        if c not in answer:
            answer.append(c)

    return "".join(answer)