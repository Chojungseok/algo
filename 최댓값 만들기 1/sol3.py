# 버블 정렬
## 앞의 두 수를 비교하여 큰 수가 뒤로 가게끔 위치를 바꿈
## 위의 과정을 모두 제자리에 정렬이 될 때가지 반복

def solution(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers[-1] * numbers[-2]