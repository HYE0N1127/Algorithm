# 백준 12605 : 단어순서 뒤집기

from collections import deque

N = int(input())
for i in range(N):

    L = input().split()
    d = deque(L)

    print(f'Case #{i+1}:', end=' ')

    while len(d) > 0:
        print(d.pop(), end=' ')