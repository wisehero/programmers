gpa = 0  # 평점
hakjum = 0
d = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

for _ in range(20):
    subject, x, y = input().split(" ")
    if y != "P":
        hakjum += float(x)
        gpa += float(x) * d[y]

print(round(gpa / hakjum, 6))
