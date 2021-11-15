# Programmers Level 1 나머지가 1이 되는 수 찾기

import math

def solution(n):
    max = n - 1
    if max % 2 == 0:
        return 2
    else :
        for i in range(2, int(math.sqrt(max)) + 1):
            if max % i == 0:
                return i
    return max