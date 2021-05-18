i = 0
j = 0

n = input()
m = input()

for i in range(int(m)):
    for j in range(int(n)):
        print('*', end='')      # Python print 함수는 자동 줄바꿈을 해주기에 끝부분을 어떤 식으로 해줄 지 정의해줘야합니다.
    print()