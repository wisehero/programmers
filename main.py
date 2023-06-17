def solution(box, n):
    answer = 0

    w_count, h_count = box[0] // n, box[1] // n

    semi_result = w_count * h_count
    answer = semi_result * (box[2] // n)

    return answer
