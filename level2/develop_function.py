'''
1. 각 기능은 100% 일때 서비스에 반영한다.
2. 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있다.
3. 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포된다.

'''
import collections
import copy


def solution(progresses, speeds):
    answer = []
    # 각 progress와 대응하는 speed를 더해준다.
    # 맨 앞의 작업이 100이상이면 디큐 전체를 검사해서
    # 100 이상인 작업은 전부 팝
    # 작업완료 횟수 1 증가
    # 큐가 전부 빌 때까지 반복
    front = 0
    count = 1

    for i in range(100):
        for j in range(len(progresses)):
            progresses[j] += speeds[j]

        if progresses[front] >= 100:
            for k in range(front + 1, len(progresses)):
                if progresses[k] >= 100:
                    front += 1
                    count += 1
                else:
                    break
            front += 1
            answer.append(count)

            count = 1

        if front == len(progresses):
            print(answer)
            break
    return answer



print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
