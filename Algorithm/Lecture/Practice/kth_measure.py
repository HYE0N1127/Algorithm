n, k = map(int, input("숫자 두 개를 입력해주세요 : ").split())
list = []
cnt = 0

# 강의 풀의

for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:              # For - Else 문으로 For 문이 정상적으로 반복을 완료하면 시작하는 구문
    print(-1)