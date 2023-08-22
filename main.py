def solution(info, query):
    answer = []

    for q in query:
        q = q.split(" and ")
        lang = q[0]
        position = q[1]
        career = q[2]
        soulfood, score = q[3].split(" ")
        count = 0

        for i in info:
            c_lang, c_position, c_career, c_soulfood, c_score = i.split(" ")
            if lang == c_lang or lang == "-":
                if position == c_position or position == "-":
                    if c_career == career or career == "-":
                        if soulfood == c_soulfood or soulfood == "-":
                            if int(score) <= int(c_score) or score == "-":
                                count += 1

        answer.append(count)

    return answer


solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
          "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
         ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
          "- and - and - and - 150"])
