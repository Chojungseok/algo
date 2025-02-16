def solution(numbers):
    answer = 0

    total = 0 ## numbers의 모든 값의 합을 저장
    i = 0 ## 1회 반복 할때마다 1을 더해줌으로써 numbers 가 같고 있는 데이터의 갯수를 확인 할 수 있음

    for number in numbers:
        total = total + number
        i = i + 1

    answer = total / i

    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))
