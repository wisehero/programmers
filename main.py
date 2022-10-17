def solution(music):
    answer = 0
    now_position = 1
    black = [2, 4, 6, 9, 11]
    d = {1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 3, 8: 4, 9: 5, 10: 5, 11: 6, 12: 6}
    for i in music:
        if now_position == 1:
            answer += d[i]
            now_position = i
        else:
            if i == now_position + 1 or i == now_position - 1:
                answer += 1
                now_position = i
            else:
                if i in black:
                    answer += abs(d[now_position] - d[i]) + 1
                    now_position = i

                else:
                    answer += abs(d[now_position] - d[i])
                    now_position = i

    return answer


print(solution([10,9,4,5,12]))
