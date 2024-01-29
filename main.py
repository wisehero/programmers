# 국어점수가 감소하는 순서로 먼저 정렬
# 국어 점수가 같으면 영어 점수 오름차순
# 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서


n = int(input())
arr = []

for _ in range(n):
    name, korean, english, math = input().split()
    korean = int(korean)
    english = int(english)
    math = int(math)
    arr.append([name, korean, english, math])

arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for a in arr:
    print(a[0])
