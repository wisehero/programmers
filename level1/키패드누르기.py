def solution(numbers, hand):
    answer = ''

    keypad = {
        1: [1, 1],
        2: [1, 2],
        3: [1, 3],
        4: [2, 1],
        5: [2, 2],
        6: [2, 3],
        7: [3, 1],
        8: [3, 2],
        9: [3, 3],
        "*": [4, 1],
        0: [4, 2],
        "#": [4, 3]
    }

    left_hand = keypad["*"]
    right_hand = keypad["#"]

    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            left_hand = keypad[num]
        elif num in [3, 6, 9]:
            answer += "R"
            right_hand = keypad[num]
        else:
            rd = abs(right_hand[1] - keypad[num][1]) + abs(right_hand[0] - keypad[num][0])
            ld = abs(left_hand[1] - keypad[num][1]) + abs(left_hand[0] - keypad[num][0])
            if ld < rd:
                answer += "L"
                left_hand = keypad[num]
            elif ld > rd:
                answer += "R"
                right_hand = keypad[num]
            else:
                if hand == "right":
                    answer += "R"
                    right_hand = keypad[num]
                else:
                    answer += "L"
                    left_hand = keypad[num]
    return answer