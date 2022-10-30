from collections import Counter


def solution(id_list, report, k):
    answer = []
    report_dict = dict()
    reported_id = []

    for key in id_list:
        report_dict[key] = []

    for case in report:
        case = case.split(" ")
        if case[1] not in report_dict[case[0]]:
            report_dict[case[0]].append(case[1])
            reported_id.append(case[1])

    reported_id = Counter(reported_id)

    for person in id_list:
        mail = 0
        for value in report_dict[person]:
            if reported_id[value] >= k:
                mail += 1
        answer.append(mail)
    return answer


def solution_2(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x: 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
