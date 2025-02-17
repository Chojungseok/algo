def solution(my_string, letter):
    return ''.join([i for i in my_string if i != letter])


### list comprehension을 활용하여 코드 단축