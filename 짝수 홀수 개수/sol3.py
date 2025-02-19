# 홀수의 개수만 확인 하여 전체 데이터 개수에서 - 홀수 갯수 = 짝수 개수
def solution(num_list):
    odd_num = sum(i % 2 for i in num_list)
    answer = [len(num_list) - odd_num, odd_num]
    return answer