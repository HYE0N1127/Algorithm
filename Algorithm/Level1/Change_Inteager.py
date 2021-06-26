# Programmers Level 1 - 문자열 정수로 변환하기

def solution(s):
    answer = int(s)

    return answer


# Best Answer
def otherSolution(str):
    result = 0

    for idx, number in enumerate(str[::-1]):  # 주어진 스트링을 거꾸로 만든 후 enumerate 함수를 지정하여 한 글자당 인덱스 배정
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)  # 그 후 각 자리에 10의 지수만큼 곱해줌

    return result


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(otherSolution("-1234"))  # EX) -1234 = 4321- -> 4 * (10 ** 0) + 3 * (10 ** 1) + 2 * (10 **2) + 1 * (10 ** 3) -> - 일 시에 -1을 곱하여 부호를 바꿈
