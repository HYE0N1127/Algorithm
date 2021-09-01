# 백준 2869번 달팽이는 올라가고 싶다

L1 = input()

A, B, V = map(int, L1.split())
d = 0
p = 0

d = A - B
p = V - B

count = p // d
if p % d > 0:
    count += 1

print(count)