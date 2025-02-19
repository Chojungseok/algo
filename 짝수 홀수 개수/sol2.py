# 2로 나눈 나머지를 활용한 indexing으로 개수 도출
def solution(num_list):
    answer = [0,0]
    for i in num_list:
        answer[i % 2] += 1
    return answer