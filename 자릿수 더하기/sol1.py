def solution(n):
    answer = 0
    str_n = str(n)
    for i in str_n:
        answer += int(i)
    return answer

### 입력받은 n을 문자형으로 바꾼다음 for 문을 통해서 한개씩 Int형으로 바꾸어 answer에 더하기