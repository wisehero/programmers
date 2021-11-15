def solution(s):
    answer = ''
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    # 확인 문자열
    check_word = ''
    # 문자는 숫자로
    for i in s:
        # 들어온 문자열이 문자인지 판단
        if i.isalpha():
            # 문자이면 check_word에 넣어놓기
            check_word += i
            # 만약 문자열이 words 리스트 안에서 확인이 되면
            if check_word in words and 3 <= len(check_word) <= 5:
                # 해당 문자열의 인덱스를 찾아 nums에 대응되는 수를 찾고 문자열로 변환하여 answer에 붙여줌
                answer += str(nums[words.index(check_word)])
                # 그리고 check_word는 다시 초기화
                check_word = ''
        else:
            # 숫자는 숫자그대로 넣으면 된다.
            answer += i
    return int(answer)


print(solution("one4seveneight"))
