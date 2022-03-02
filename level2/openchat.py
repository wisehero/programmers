def solution(record):
    answer = []
    d = dict()
    for i in record:
        i = i.split(" ")
        if len(i) == 3:
            d[i[1]] = i[2]

    for i in record:
        i = i.split()
        if i[0] == "Enter":
            answer.append(d[i[1]] + "님이 들어왔습니다.")
        if i[0] == "Leave":
            answer.append(d[i[1]] + "님이 나갔습니다.")

    return answer
