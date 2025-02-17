def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if i != letter:
            answer += i
    return answer


## letter에 제거 하고자 하는 데이터가 주어지므로 my_string을 반복했을때 letter와 같지 않다면 answer에 입력