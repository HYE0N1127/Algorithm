# Programmers Level 1 가장 작은 수 제거하기

def solution(arr):
    answer = []
    low = min(arr)

    if len(arr) == 1:
        return [-1]

    for i in arr:
        if low != i:
            answer.append(i)

    return answer