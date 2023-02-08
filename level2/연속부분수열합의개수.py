def solution(elements):
    answer = 0
    elements_circle = elements * 2
    sum_set = set()
    for i in range(len(elements)):
        for j in range(len(elements), 0, -1):
            sub_list = elements_circle[i:i+j]
            sum_set.add(sum(sub_list))
    answer = len(sum_set)
    return answer


solution([7, 9, 1, 1, 4])
