a = input()
b = input()
nums = ''

for i in range(len(a)):
    nums += a[i]
    nums += b[i]

temp = ''
i = 0
while True:
    temp += str(int(nums[i]) + int(nums[i + 1]))[-1]
    i += 1

    if i == len(nums) - 1:
        i = 0
        nums = temp
        temp = ''

    if len(nums) <= 2:
        break
print(nums)


