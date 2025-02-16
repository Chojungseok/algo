def solution(n):
    answer = 0

    for i in range(2, n+1, 2): # 2부터 n+1까지 2개 단위로 덧셈
        answer += i

    return answer

print(solution(10))
print(solution(4))