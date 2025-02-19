# for문과 if문을 활용한 풀이
def solution(num_list):
    answer = []
    even_num = 0
    odd_num = 0
    for i in num_list:
        if i % 2 == 0:
            even_num += 1
        else :
            odd_num += 1

    answer.append(even_num)
    answer.append(odd_num)
    return answer


# append 2개 사용 -> extend로 수정
def solution(num_list):
    answer = []
    even_num = 0
    odd_num = 0
    for i in num_list:
        if i % 2 == 0:
            even_num += 1
        else :
            odd_num += 1

    answer.extend([even_num, odd_num])
    return answer