# 프로그래머스 Level 1 이상한 문자열 만들기
def solution(s):
    s_split = s.split(" ")

    for k in range(len(s_split)):
        s_list = list(s_split[k])

        for i in range(len(s_list)):
            if i % 2 == 0:
                s_list[i] = s_list[i].upper()

            elif i % 2 == 1:
                s_list[i] = s_list[i].lower()
        s_split[k] = "".join(s_list)

    answer = " ".join(s_split)

    return answer


if __name__ == '__main__':
    print(solution("try hello world"))
