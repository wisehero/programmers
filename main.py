n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

answer = 0
for a in arr:
    a = list(a)
    stack = []
    while a:
        stack.append(a.pop())
        # 스택의 길이가 2 이상이고 스택의 맨 마지막과 그 전에 요소가 같으면 반복
        while len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    # 스택이 비어있으면 좋은 단어
    if not stack:
        answer += 1

print(answer)
