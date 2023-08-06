t = int(input())
d = {}
for _ in range(t):
    name, record = input().split(" ")
    d[name] = record

in_company = []
for key in d.keys():
    if d[key] == "enter":
        in_company.append(key)

in_company.sort(reverse=True)

for emp in in_company:
    print(emp)
