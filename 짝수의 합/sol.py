def solution(n):
    answer = 0

    for i in range(n+1): ## n-1의 값이 출력이 되기 때문에 n까지 포함해서 숫자의 합을 알고 싶을 경우 +1을 해주면 된다.
        if i % 2 == 0:
            answer = answer + i
            # answer += i

    return answer

print(solution(10))
print(solution(4))