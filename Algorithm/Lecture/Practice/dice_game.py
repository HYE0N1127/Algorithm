import sys

sys.stdin = open("input/dice_game/input.txt", "rt")

n = int(input())
res = 0

for i in range(n):

    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)

    if a == b and b == c:
        sum = 1000 * a + 10000

    elif a == b or a == c:
        sum = 100 * a + 1000

    elif b == c:
        sum = 100 * b + 1000

    else:
        sum= c * 100   # Sort를 통하여 C를 가장 큰 수로 올렸기때문에 C * 100

    if sum > res:
        res = sum


print(res)
