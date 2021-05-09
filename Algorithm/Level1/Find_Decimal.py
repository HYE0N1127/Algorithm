# 소수 찾기
def solution(n):
    j = 0
    i = 0
    result = 0

    while i == n:
        while j == n:
            i += 1
            j += 1
            if i / j == 1 and i / 1 == 0:
                result += 1

    return result


if __name__ == '__main__':
    print(solution(7))
