times = []
for _ in range(4):
    times.append(int(input()))

amount = sum(times)
minutes = amount // 60
seconds = amount % 60
print(minutes)
print(seconds)
