# Programmers Level 1 - 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []

    for item in arr:

        if item % divisor == 0:
            answer.append(item)

        if len(answer) == 0:
            answer.append(-1)
        else:
            answer.sort()

        return answer

# Test Function for test case
if __name__ == '__main__':
    print(solution([1, 2, 3, 4], 2))
