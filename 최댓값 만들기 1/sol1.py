def solution(numbers):
    answer = 0
    numbers.sort(reverse = True)
    max_1, max_2 = numbers[0], numbers[1]
    answer = max_1 * max_2
    return answer