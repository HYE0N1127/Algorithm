# 백준 9012 : 괄호
from collections import deque

N = int(input())
for i in range(N):
    L = input()
    opened = 0
    for p in L:
        if p == '(':
            opened += 1
        elif opened > 0:
            opened -= 1
        else:
            print('NO')
            break
    else:  # break 를 사용하지 않고 루프가 끝났을 때
        print('YES' if opened == 0 else 'NO')
