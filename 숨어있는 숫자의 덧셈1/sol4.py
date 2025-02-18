### ord(값): 글자가 컴퓨터가 이해하는(ASCII)언어로 바꾸었을때 몇번째에 있는지를 출력해줌(65 ~ 122의 값이 나오면 문자라는 것을 알 수 있다)

def solution(my_string):
    answer = 0

    for char in my_string:
        if not (ord('A') <= ord(char) <= ord('Z')) :
            answer += int(char)
    return answer

