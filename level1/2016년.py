def solution(a, b):
    d = {}
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    c = 0
    for i in range(1, 13):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            end_day = 31
        elif i in [4, 6, 9, 11]:
            end_day = 30
        else:
            end_day = 29

        for j in range(1, end_day + 1):
            d[f"{i}{j}"] = day[c % len(day)]
            c += 1

    print(d)
    dt = str(a) + str(b)
    return d[dt]
