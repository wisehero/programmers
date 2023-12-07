def solution(bandage, health, attacks):
    answer = 0  # 남은 체력
    t, cure, bonus = bandage
    max_health = health
    d = {x: y for x, y in attacks}
    max_time = max(d.keys())

    time = 0
    cure_continue = 0

    while time < max_time and health > 0:
        time += 1
        if time in d:
            health -= d[time]
            cure_continue = 0
            print(time, health, cure_continue)
            continue

        health = min(health + cure, max_health)
        cure_continue += 1

        if cure_continue == t:
            health = min(health + bonus, max_health)
            cure_continue = 0

        print(time, health, cure_continue)
    if health <= 0:
        answer = -1
    else:
        answer = health
    return answer
