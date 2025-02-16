def solution(numbers):
    answer = 0

    answer = sum(numbers) / len(numbers) ## sum()함수를 하용하면 ()안의 변수에 저장 되어있는 리스트의 모든 값의 합을 구할 수 있음 / len()함수를 하용하면 ()안에이는 변수가 같고 있는 데이터의 갯수(길이)를 확인 할 수 있음

    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))
