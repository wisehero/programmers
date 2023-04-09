"""
그냥 스택으로 푸는게 좋다.
숫자 더해주고 빼는 식으로 하면
분기가 너무 나뉘어진다.
"""


def solution(s):
    answer = 0
    temp = list(s)

    for _ in range(len(s)):

        stack = []
        for i in range(len(temp)):
            if len(stack) > 0:
                if stack[-1] == '[' and temp[i] == ']':
                    stack.pop()
                elif stack[-1] == '(' and temp[i] == ')':
                    stack.pop()
                elif stack[-1] == '{' and temp[i] == '}':
                    stack.pop()
                else:
                    stack.append(temp[i])
            else:
                stack.append(temp[i])
        if len(stack) == 0:
            answer += 1
        temp.append(temp.pop(0))
    return answer


print(solution("[)(]"))
