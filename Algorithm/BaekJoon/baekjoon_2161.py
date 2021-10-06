# 백준 2161 : 카드 1
from collections import deque

n = int(input())
list = deque(range(1, n + 1))

while len(list) > 1:
    print(list.popleft(), end=' ')
    list.append(list.popleft())

print(list.pop())

