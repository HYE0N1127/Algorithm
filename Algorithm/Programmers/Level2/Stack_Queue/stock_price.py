# Programmers Level 2 주식가격
from collections import deque

# 자신의 풀이
def solution(prices):
    cnt = 0
    answer = []

    for i in range(len(prices)):
        cnt = 0
        for j in range(i + 1, len(prices)):     # i 값 앞의 index를 돌아야 하기에 i + 1로 시작 값을 정해줌
            if prices[i] <= prices[j]:      # price 의 i 번째 index가 j 번째 index보다 크다면 cnt 값 증감
                cnt += 1
            else:       # 이 외의 경우 가격이 1초간 높은 것이기에 cnt 변수에 1 추가 후 break
                cnt += 1
                break

        answer.append(cnt)

    return answer

# 생각하는 이상적인 풀이
def solution(prices):
    answer = []
    prices = deque(prices)      # Price List 를 Deque List 로 만듬
    while prices:
        c = prices.popleft()        # popleft는 값이 Return 되는 Callback 내장함수이기에 c에 가격을 저장해둠

        count = 0
        for i in prices:
            if c > i:       # 1초간 가격이 제일 높았기에 cnt 변수에 1 추가
                count += 1
                break
            count += 1      # 해당 경우가 아니라면 계속하여 cnt 변수에 1 추가

        answer.append(count)

    return answer