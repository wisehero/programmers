def solution(N, stages):
    answer = []
    d = {}

    for i in range(1, N + 1):
        d[i] = 0

    for stage in stages:
        if stage > N:
            continue
        d[stage] += 1

    m = len(stages)

    for stage in d.keys():
        if m <= 0:
            d[stage] = 0
            continue
        a = d[stage]
        d[stage] /= m
        m -= a

    fail = sorted(d.items(), key=lambda x: -x[1])

    for f in fail:
        answer.append(f[0])

    return answer
