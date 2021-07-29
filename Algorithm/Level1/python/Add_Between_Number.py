def solution(a, b):
    answer = 0

    if a < b:
        answer = sum(list(range(a, b + 1)))
        # List 자료형으로 만들어준 다음 a부터 b까지의 수를 더해줌

    else:
        answer = sum(list(range(b, a + 1)))

    return answer