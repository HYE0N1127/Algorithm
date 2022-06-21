import copy
import sys
from collections import deque

# sys.stdin = open("input/resque_princess/input.txt", "r")

n, k = map(int, input().split())
l = list(range(1, n + 1))
deque = deque(l)

while deque:
    for _ in range(k - 1):
        element = deque.popleft()
        deque.append(element)

    deque.popleft()

    if len(deque) == 1:
        print(deque[0])
        deque.popleft()
