import sys

sys.stdin = open("input/decimal/input.txt", "rt")

n = int(input())
ch = [0] * (n + 1)  # N의 값을 이용하여 1차원 배열 생성
cnt = 0

for i in range(2, n):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n + 1, i):
            ch[j] = 1       # 특정 수의 배수는 소수가 될 수 없기에 제외함
print(cnt)