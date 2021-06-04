# Programmers level 1 - 두 정수 사이의 합 구하기

def solution(a, b):
    answer = 0

    if a < b:
        answer = sum(list(range(a, b + 1)))
        # List로 변환 후 a부터 b의 값의 합을 구해줌

    else:
        answer = sum(list(range(b, a + 1)))

    return answer
