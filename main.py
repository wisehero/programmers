n = int(input())
arr = list(map(int, input().split()))

switch = []
for i in range(len(arr)):
    switch.append([i + 1, arr[i]])

person = int(input())
people = []

for _ in range(person):
    a, b = map(int, input().split())
    people.append([a, b])

for a, b in people:
    if a == 1:
        for i in range(len(switch)):
            if switch[i][0] % b == 0:
                if switch[i][1] == 1:
                    switch[i][1] = 0
                else:
                    switch[i][1] = 1

    if a == 2 and len(switch) >= 3:

        start = 0
        end = 0
        selection = b - 1
        i = 1

        if selection == 0 or selection == len(switch) - 1:
            if switch[selection][1] == 1:
                switch[selection][1] = 0
            else:
                switch[selection][1] = 1

            continue
        while switch[selection - i][1] == switch[selection + i][1]:
            start = selection - i
            end = selection + i
            i += 1
            if start == 0 or end == len(switch) - 1:
                break

        if 0 <= start < end:
            for i in range(start, end + 1):
                if switch[i][1] == 0:
                    switch[i][1] = 1
                else:
                    switch[i][1] = 0
        else:
            if switch[selection][1] == 1:
                switch[selection][1] = 0
            else:
                switch[selection][1] = 1

for i in range(len(switch)):
    print(switch[i][1], end=" ")
    if i % 20 == 19:
        print()
