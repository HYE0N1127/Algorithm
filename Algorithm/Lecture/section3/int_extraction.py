import sys
import re

sys.stdin = open("input/int_extraction/input.txt", "rt")

res = 0
cnt = 0
s = input()
numbers = int(re.sub(r'[^0-9]', '', s))     # 문자열에서 숫자를 한개의 문자열로 추출하는 정규식

# for x in s:
#     if x.isdecimal():
#         res = res * 10 + int(x)
# 숫자로 만드는 두번째 식

for i in range(1, numbers + 1):
    if numbers % i == 0:
        cnt += 1

print(numbers)
print(cnt)
