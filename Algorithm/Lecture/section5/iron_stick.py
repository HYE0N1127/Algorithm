import sys

sys.stdin = open("input/iron_stick/input.txt")

s = input()
stack = []
cnt = 0

for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])

    else:
        stack.pop()
        if s[i - 1] == "(":
            cnt += len(stack)       # Stack에 남아있는 토막의 갯수기에 cnt를 stack의 길이만큼 증가시킴
        else:
            cnt += 1
print(cnt)
