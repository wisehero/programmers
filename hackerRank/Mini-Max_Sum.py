def miniMaxSum(arr):
    # Write your code here
    answer = []
    arr.sort()
    answer.append(sum(arr[:len(arr) - 1]))
    answer.append(sum(arr[1:]))

    print(*answer)
