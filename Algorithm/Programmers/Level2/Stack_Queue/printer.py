# Programmers Level 2 프린터

from collections import deque

def solution(priorities, location):
    cnt = 0
    d = deque([(v, i) for i, v in enumerate(priorities)])       # enumerate 를 통하여 리스트의 값과 index 값을 동시에 저장

    while len(d):
        item = d.popleft()      # popleft는 CallBack 함수 이기에 item에 pop 후 저장

        if d and max(d)[0] > item[0]:       # d 의 Max 값이 item의 값보다 크다면 우선순위가 낮은 것이기에 다시 Append 시킴
            d.append(item)
        else:
            cnt += 1        # 1 회를 돌았기에 Cnt 값 증가
            if item[1] == location:     # 만약 아이템이 location 의 위치와 같다면
                break       # Break
    return cnt
