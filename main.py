def solution(num_list, n):
    answer = []
    li = []
    for i in range(len(num_list)):
        if (i + 1) % n == 0:
            li.append(num_list[i])
            answer.append(li)
            li = []
        else:
            li.append(num_list[i])
    return answer