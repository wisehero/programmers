def solution(command):
    answer = [0, 0]
    direction = 0

    for c in command:
        if c in "RL":
            if c == "R":
                direction += 1
            else:
                direction -= 1
        else:
            if c == "G":
                if direction % 4 == 0:
                    answer[1] += 1
                elif direction % 4 == 1:
                    answer[0] += 1
                elif direction % 4 == 2:
                    answer[1] -= 1
                else:
                    answer[0] -= 1
            else:
                if direction % 4 == 0:
                    answer[1] -= 1
                elif direction % 4 == 1:
                    answer[0] -= 1
                elif direction % 4 == 2:
                    answer[1] += 1
                else:
                    answer[0] += 1

    return answer
