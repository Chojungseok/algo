def solution(my_string):
    answer = 0
    for i in my_string:
        try:
            answer += int(i)
        except:
            pass
    return answer

### try - except활용 try: 시도할 내용, except: try가 오류 났을떄 실행 할 내용