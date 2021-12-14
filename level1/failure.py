def solution(N, stages):
    answer = []
    past_stage = 0
    result = []
    for i in range(1, N + 1):
        if i in stages:
            answer.append((i, stages.count(i) / (len(stages) - past_stage)))
            past_stage += stages.count(i)
        else:
            answer.append((i, 0))
    answer.sort(reverse=True, key=lambda x: x[1])
    for i in answer:
        result.append(i[0])
    return result
