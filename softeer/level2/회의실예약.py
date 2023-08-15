rooms, reserved = map(int, input().split(" "))

room_name = []
for _ in range(rooms):
    room_name.append(input())
room_name.sort()

# 회의실 이름 정렬해둔걸 기반으로 09~18시까지의 회의실 사용가능 여부 기록
d = {x: [0] * 18 + [1] for x in room_name}

for _ in range(reserved):
    r_name, r_start, r_end = input().split(" ")
    r_start = int(r_start)
    r_end = int(r_end)
    for i in range(r_start, r_end):
        d[r_name][i] = 1

for index, room in enumerate(d):
    print(f'Room {room}:')
    is_start = 1
    times = []
    for i in range(9, 19):
        if d[room][i] == 0 and is_start == 1:
            start = i
            is_start = 0
        elif d[room][i] == 1 and is_start == 0:
            end = i
            is_start = 1
            times.append([start, end])
    if len(times) == 0:
        print('Not available')
    else:
        print(f'{len(times)} available:')
        for x in times:
            print(f'{x[0]:02d}-{x[1]}')

    if index != len(d) - 1:
        print('-----')

