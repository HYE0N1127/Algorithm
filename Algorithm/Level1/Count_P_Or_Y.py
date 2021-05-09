# 문자열 내에서 소문자, 대문자 P와 Y의 개수를 세어서 둘의 개수가 같으면 True, 아니면 False return 해주기

def solution(s):
    p = 0
    y = 0
    i = 0

    while s is None:
        if s[i] == "p" or s[i] == "P":
            p += 1
        elif s[i] == "y" or s[i] == "Y":
            y += 1

        i += 1

    if p == y:
        return 'True'
    else:
        return 'False'


if __name__ == '__main__':
    string = input("문자를 입력해주세요 : ")
    print(solution(string))
