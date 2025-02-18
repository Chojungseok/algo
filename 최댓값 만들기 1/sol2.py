def solution(numbers):
    answer = 0
    max_1 = max(numbers)
    numbers.pop(numbers.index(max_1))
    max_2 = max(numbers)
    answer = max_1 * max_2
    return answer