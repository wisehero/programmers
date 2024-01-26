a, b = map(int, input().split())
arr = list(map(int, input().split()))

answer = [sum(arr[:b])]  # O(n)

for i in range(len(arr) - b):
    amount = answer[i] - arr[i] + arr[i + b]
    answer.append(amount)

print(max(answer))
