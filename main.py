while True:
    numbers = list(map(int, input().split()))
    numbers.sort()
    if numbers[0] == 0 and numbers[1] == 0 and numbers[2] == 0:
        break
    if pow(numbers[0], 2) + pow(numbers[1], 2) == pow(numbers[2], 2):
        print("right")
    else:
        print("wrong")
