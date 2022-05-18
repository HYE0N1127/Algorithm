# Programmers Level 2 기능개발

def solution(progresses, speeds):
    q = []
    cnt = 1

    # Queue 에다가 기능개발 일수를 넣는 코드
    for i in range(len(progresses)):
        percent = 100 - progresses[i]
        if percent % speeds[i] != 0:
            days = percent // speeds[i] + 1
            q.append(days)
        else:
            days = percent // speeds[i]
            q.append(days)

    answer = []

    # first 변수를 만들어서 첫번째 변수 값을 넣어둔 뒤에 1부터 for문을 돌려서 다음 날에 접근
    first = q[0]
    for i in range(1, len(q)):
        # 같거나 더 크다면 하루를 추가해줌
        if first >= q[i]:
            cnt += 1
        # 아니라면 cnt값을 answer에 넣어주고 first 변수를 q의 i번째 인덱스로 넣어준 후에 cnt 변수 1로 초기화
        else:
            answer.append(cnt)
            first = q[i]
            cnt = 1
    answer.append(cnt)

    return answer
