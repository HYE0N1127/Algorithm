# Programmers Level 1 - 가운데 글자 가져오기

def solution(s):
    answer = ''
    length = len(s)
    middle = length // 2

    if length % 2 == 0:
        answer = s[middle - 1: middle + 1]
    elif length % 2 == 1:
        answer = s[middle]

    return answer


# Main Function for test case
if __name__ == '__main__':

    print(solution("abced"))
    print(solution("qwer"))
