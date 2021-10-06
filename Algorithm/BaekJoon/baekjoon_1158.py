# 백준 1158 : 요세푸스 문제
from collections import deque

N, K = map(int, input().split())

circle = deque(range(1, N + 1))
pile = deque()

while len(circle) > 1:
    for i in range(K - 1):
        circle.append(circle.popleft())
    pile.append(circle.popleft())

pile.append(circle.popleft())

print('<' + ', '.join(map(str, pile)) + '>')