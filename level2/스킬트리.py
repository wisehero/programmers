from collections import deque


def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_tree = deque(skill_tree)
        i = 0
        while True:
            if len(skill_tree) == 0:
                break
            one = skill_tree.popleft()
            if one in skill and one == skill[i]:
                i += 1
                continue
            elif one in skill and one != skill[i]:
                skill_tree.appendleft(one)
                break

        if len(skill_tree) == 0:
            answer += 1

    return answer


def solution_v2(skill, skill_tree):
    answer = 0
    for i in skill_tree:
        skill_list = ''
        for z in i:
            if z in skill:
                skill_list += z
        if skill_list == skill[0:len(skill_list)]:
            answer += 1
    return answer
