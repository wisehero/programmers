# ext에 의해 데이터를 뽑아내고 val_ext로 뽑아낼 정보의 기준값을 정한다.
def solution(data, ext, val_ext, sort_by):
    answer = []
    pick_index = 0

    if ext == "code":
        pick_index = 0
    elif ext == "date":
        pick_index = 1
    elif ext == "maximum":
        pick_index = 2
    else:
        pick_index = 3

    for one_data in data:
        if one_data[pick_index] < val_ext:
            answer.append(one_data)

    if sort_by == "code":
        answer.sort(key=lambda x: x[0])
    elif sort_by == "date":
        answer.sort(key=lambda x: x[1])
    elif sort_by == "maximum":
        answer.sort(key=lambda x: x[2])
    else:
        answer.sort(key=lambda x: x[3])

    return answer
