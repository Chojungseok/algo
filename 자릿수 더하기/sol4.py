def solution(n):
    answer =  sum(map(int, list(str(n))))
    return answer


print(solution(1234))