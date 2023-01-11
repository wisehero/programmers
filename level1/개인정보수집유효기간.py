def solution(today, terms, privacies):
    answer = []

    year, month, day = today.split(".")
    today = int(year) * 12 * 28 + int(month) * 28 + int(day)

    terms = {i[:1]: int(i[2:]) * 28 for i in terms}

    for i, p in enumerate(privacies):
        y, m, d = p.split(".")
        d, c = d.split()

        p = int(y) * 12 * 28 + int(m) * 28 + int(d)
        if p + terms[c] <= today:
            answer.append(i + 1)
    return answer


solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
