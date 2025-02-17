def solution(my_string):
    answer = 0
    num_list = ['0','1','2','3','4','5','6','7','8','9']
    for i in my_string:
        if i in num_list:
            answer += int(i)
    return answer

### 0~9까지 한자리수의 숫자를 모두 문자형으로 하여 리스트에 저장한뒤 입력받은 my_string을 반복하여 num_list에 있을 경우 int형으로 전환하여 answer에 더하기