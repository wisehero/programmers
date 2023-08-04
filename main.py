def solution(arr1, arr2):
    answer = []
    li = []
    row , col = len(arr1), len(arr1[0])
    for i in range(row):
        for j in range(col):    
            li.append(arr1[i][j] + arr2[i][j])            
            if j == col-1:
                answer.append(li)
                li = []
    return answer