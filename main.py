# 모든 달은 28일까지 있다.
def solution(today, terms, privacies):
    answer = []
    terms_dic = {}
    for term in terms:
        a, b = term.split(" ")
        terms_dic[a] = int(b) * 28

    year, month, day = today.split(".")

    today = int(day) + (int(month) * 28) + (int(year) * 28 * 12)

    for privacy in privacies:
        date, term = privacy.split(" ")
        date_year, date_month, date_day = date.split(".")

        date_time = int(date_day) + (int(date_month) * 28) + (int(date_year) * 28 * 12)
        date_time += terms_dic[term]

        if date_time < today:
            answer.append(privacies.index(privacy) + 1)

    return answer

solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])