# 학생 수는 항상 짝수다
# 두 학생 이상의 득점이 동일할 때는 번호가 낮은 학생을 우선적으로 우반에 편성한다.

def solution(n, student, point):
    answer = 0
    student_point = zip(student, point)
    dictionary = {student_number: 0 for student_number in range(1, n + 1)}
    mid = n // 2
    now_rank = list(range(1, n + 1))
    for pair in student_point:
        before_student_rank = now_rank.index(pair[0])
        dictionary[pair[0]] += pair[1]
        sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
        updated_dictionary = dict(sorted_dictionary)
        now_rank = list(updated_dictionary.keys())
        after_student_rank = now_rank.index(pair[0])
        if after_student_rank != before_student_rank:
            if before_student_rank >= mid > after_student_rank:
                answer += 1
        else:
            continue

    return answer
