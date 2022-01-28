def solution(citations):
    answer = 0
    n = len(citations)
    for i in range(n - 1, -1, -1):  # 끝에서 부터 출발
        h = i + 1
        cnt_use = 0
        cnt_notuse = 0
        for j in citations:
            if j <= h:
                cnt_notuse += 1
            if j >= h:
                cnt_use += 1
        if cnt_use >= h and cnt_notuse <= h:
            answer = h
            break
    return answer


solution([3, 0, 6, 1, 5])
