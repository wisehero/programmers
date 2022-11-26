def solution(n, cores):
    answer = 0
    # 마지막 작업이 큐에 들어가는 시간을 찾아내는 이분탐색 실시
    low = n // len(cores) * min(cores)
    high = n * min(cores)
    mid = (low + high) // 2
    while low < high:
        cnt = 0
        avail = 0
        for core in cores:
            cnt += mid // core + 1
            # mid 시간 도달 직전까지 해당 코어의 수행 작업 수 검사
            if mid % core == 0:
                avail += 1
                cnt -= 1
        # 총 수행 작업이 n개 이상이면 high를 mid로 조정
        if cnt >= n:
            high = mid
        # 총 수행 작업과 삽입 가능 코어의 개수가 n보다 작으면 low를 mid+1로 조정
        elif cnt + avail < n:
            low = mid + 1
        # 그렇지 않은 경우(조건에 맞는 mid 시간 발견 시)에는
        else:
            # 각 코어 별 수행 작업수 계산
            for i in range(len(cores)):
                if mid % cores[i] == 0:
                    cnt += 1
                # cnt와 n이 일치하면 해당 코어의 번호 리턴
                if cnt == n:
                    return i + 1
        # mid 재조정 후 반복문을 다시 돎
        mid = (low + high) // 2
    return answer
