# 백준 10773 : 제로
from collections import deque

d = deque()

K = int(input())
for i in range(K):
    n = int(input())
    if n == 0:
        d.pop()
    else:
        d.append(n)

print(sum(d))