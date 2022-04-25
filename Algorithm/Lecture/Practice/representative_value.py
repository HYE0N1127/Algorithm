import sys

# sys.stdin = open("input/representative_value/input.txt", "rt")

avg: float = 0
n = int(input())
score = list(map(int, input().split()))
min = 123123123123

avg = round(sum(score) / n)  # round 내장 함수를 이용하여 반올림 진행

for idx, x in enumerate(score):
    tmp = abs(x - avg)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1

print(avg, res)