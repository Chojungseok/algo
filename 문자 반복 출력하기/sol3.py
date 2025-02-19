# for문 두개를 사용한 풀이
def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i * n
    return answer