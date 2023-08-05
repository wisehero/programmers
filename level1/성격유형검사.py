def solution(survey, choices):
    answer = ''
    d = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for type, choice in list(zip(survey, choices)):
        if choice > 5:
            d[type[1]] += choice - 4
        else:
            d[type[0]] += 4 - choice

    if d["R"] >= d["T"]:
        answer += "R"
    else:
        answer += "T"

    if d["C"] >= d["F"]:
        answer += "C"
    else:
        answer += "F"

    if d["J"] >= d["M"]:
        answer += "J"
    else:
        answer += "M"

    if d["A"] >= d["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer
