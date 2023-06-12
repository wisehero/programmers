def solution(my_string):
    numbers = []
    n = ""
    for s in my_string:
        if not s.isdigit():
            if len(n) > 0:
                numbers.append(int(n))
                n = ""
        else:
            n += s
    if len(n) != 0:
        numbers.append(int(n))

    if len(numbers) == 0:
        return 0

    return sum(numbers)