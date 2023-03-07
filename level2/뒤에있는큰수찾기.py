# 스택
def solution(numbers):
    n = len(numbers)  # 전체 길이를 구한다.
    result = [-1] * n  # 결과를 모두 -1로 초기화
    stack = []
    for i in range(n - 1, -1, -1):  # 끝에서부터 반복
        # 스택이 비어있지 않고 numbers 배열의 끝에 있는
        # i 번째 숫자가 stack[-1] 번째 숫자보다 크거나 같으면 pop
        while stack and numbers[stack[-1]] <= numbers[i]:
            stack.pop()
        # 스택이 비어있지 않으면 == i번째 숫자보다 큰 수가 있으면
        if stack:
            # result의 i 번째 요소를 스택
            result[i] = numbers[stack[-1]]
        stack.append(i)
    return result


print(solution([9, 1, 5, 3, 6, 2]))

# 특정 숫자의 뒤의 배열을 따로 뽑아
# 가장 크면서
