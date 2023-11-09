# 오큰수
# 오른쪽에 있으면서 A[i]보다 큰 수중에서 가장 왼쪽에 있는 수
# 비슷한 문제 = 프로그래머스 뒤에있는 큰 수 찾기
n = int(input())
arr = list(map(int, input().split()))
answer = [0] * n
stack = []

for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)

while stack:
    answer[stack.pop()] = -1

print(*answer)
