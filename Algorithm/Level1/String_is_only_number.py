# Programmers Level 1 - 문자열은 숫자로만 이루어져 있나요?

def solution(s):
    return s.isdigit() and (len(s) == 4 or len(s) == 6)


# isdigit 함수란? : 문자열이 숫자인지 아닌지 판별해주는 함수
# 비슷한 함수는? : isalpha() 함수, 문자열이 문자인지 아닌지를 판별해줌

if __name__ == '__main__':
    print(solution("a234"))  # False
    print(solution("1234"))  # True
