def minimum_deletion_cost(S, C):
    z = list(zip(S, C))
    answer = 0

    for i in range(len(z) - 1):
        if z[i][0] == z[i+1][0]:
            answer += min(z[i][1], z[i+1][1])

    print(answer)

# Example usage
S = "ababa"
C = [10,5,10,5,10]
minimum_deletion_cost(S, C)