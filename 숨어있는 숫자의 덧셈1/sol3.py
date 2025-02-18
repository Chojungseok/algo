def solution(my_string):
    answer = []

    for char in my_string:
        if char.isdigit(): ### .isdigit() .앞에 있는 데이터가 숫자 형태로 바꿀수 있는지 확인 - 가능하면 True, 불가능 하면 False
            answer.append(int(char))
    return sum(answer)

