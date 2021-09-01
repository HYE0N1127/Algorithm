# Programmers Level 1 - 평균 구하기

def solution(arr):
    answer = 0
    addResult = 0
    length = len(arr)
    # 사소한 부분을 변수로 만들어 코드를 재활용하기

    for i in range(length):
        addResult += arr[i]
        # addResult 변수에 arr 배열의 요소를 더해주기

    answer = addResult / length

    return answer


# 테스트 메인함수
if __name__ == '__main__':
    arr = [1, 2, 4, 5]

    print(solution(arr))
