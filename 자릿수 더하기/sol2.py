def solution(n):
    answer = 0
    while n :
        answer += n % 10
        n //= 10
    return answer

### 입력 받은 n을 10으로 나누면 마지막 1의 자릿수가 항상 나머지가 된다. 그렇게 나오는 나머지들을 answer에 더해준다