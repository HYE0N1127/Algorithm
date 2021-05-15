# Programmers Level 1 - 음양 더하기

def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        result = int(absolutes[i])
        # for 문을 실행시켜 absolutes의 배열 안에 들어가있는 String 형식의 숫자를 int로 파싱해줍니다.

        if signs[i] is True:
            answer += result
            # signs에 들어가있는 속성이 True일 시에 result 변수의 값을 answer 변수에 더해줍니다.

        if signs[i] is False:
            answer += -1 * result

    return answer


# 테스트 메인함수
if __name__ == '__main__':
    absolute = [1, 4, 2, 3]
    signs = [True, False, True, False]

    print(solution(absolute, signs))
