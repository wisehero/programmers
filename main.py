def solution(today, terms, privacies):
    answer = []

    y, m, d = today.split(".")
    y = 28 * 12 * int(y)
    m = 28 * int(m)
    d = int(d)

    today = y + m + d

    dic = {}

    for term in terms:
        p, d = term.split(" ")
        dic[p] = int(d) * 28

    for i, privacy in enumerate(privacies):
        date, policy = privacy.split(" ")
        y, m, d = date.split(".")
        y = 28 * 12 * int(y)
        m = 28 * int(m)
        d = int(d)

        date = y + m + d + dic[policy]

        if date <= today:
            answer.append(i + 1)
    return answer
