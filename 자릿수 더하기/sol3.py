def solution(n):
    answer = 0
    while n:
        n, r = divmod(n, 10)
        answer += r
    return answer


### divmod를 활용하여 몫은 n, 나머지는 r에 저장하여 r을 answer에 더해준다