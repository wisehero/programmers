import math


def solution(numbers, hand):
    answer = ''
    left_hand = [1, 4, 7]
    right_hand = [3, 6, 9]
    ruled_hand = [2, 5, 8, 0]
    left_p = [(3, 0)]
    right_p = [(3, 2)]
    for num in numbers:
        # 1, 4, 7을 누를 때
        if num in left_hand:
            answer += "L"
            left_p.append((left_hand.index(num), 0))
        # 3, 6, 9를 누를 때
        if num in right_hand:
            answer += "R"
            right_p.append((right_hand.index(num), 2))
        # 가운데 2, 5, 8, 0을 누를 때,
        if num in ruled_hand:
            num_position = (ruled_hand.index(num), 1)
            # 두 점 사이의 거리를 구했을 때 더 작은 쪽에 있는 손으로
            if math.ceil(math.dist(left_p[-1], num_position)) < math.ceil(math.dist(right_p[-1], num_position)):
                answer += "L"
                left_p.append((ruled_hand.index(num), 1))
            elif math.ceil(math.dist(left_p[-1], num_position)) > math.ceil(math.dist(right_p[-1], num_position)):
                answer += "R"
                right_p.append((ruled_hand.index(num), 1))
            # 두 점 사이의 거리가 같을 때는 주로 사용하는 손으로
            else:
                answer += hand[0].upper()
                if hand == "right":
                    right_p.append((ruled_hand.index(num), 1))
                if hand == "left":
                    left_p.append((ruled_hand.index(num), 1))
    return answer
