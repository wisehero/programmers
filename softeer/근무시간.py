import sys

answer = 0

for _ in range(5):
    start, end = sys.stdin.readline().split(" ")
    start_hour, start_minute = start.split(":")
    end_hour, end_minute = end.split(":")

    start_hour, start_minute, end_hour, end_minute = int(start_hour), int(start_minute), int(end_hour), int(end_minute)

    if start_minute > end_minute:
        end_hour -= 1
        end_minute += 60

    answer += (end_minute - start_minute) + (end_hour - start_hour) * 60

print(answer)
