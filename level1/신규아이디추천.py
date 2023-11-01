def solution(new_id):
    answer = ''

    new_id = new_id.lower()

    for s in new_id:
        if s.isalnum() or s in ["-", "_", "."]:
            answer += s

        if len(answer) >= 2 and answer[-2:] == "..":
            answer = answer.replace("..", ".")

    answer = list(answer)

    if len(answer) != 0 and answer[0] == ".":
        answer.pop(0)

    if len(answer) != 0 and answer[-1] == ".":
        answer.pop()

    if len(answer) == 0:
        answer.append("a")

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer.pop()

    if len(answer) <= 2:
        while len(answer) <= 2:
            answer.append(answer[-1])

    return "".join(answer)
