# 백준 4963번 섬의 개수, DFS 문제
# 재귀함수를 이용하였기에 sys를 Import하여 재귀 최대 한도를 늘려줘야 합니다.

import sys
sys.setrecursionlimit(10 ** 5)

def dfs(x, y):
    test_map[x][y] = 2
    for i in range(8):
        target_x = dx[i] + x
        target_y = dy[i] + y

        if 0 <= target_x < h and 0 <= target_y < w and test_map[target_x][target_y] == 1:
            dfs(target_x, target_y)


dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

while True:
    w, h = map(int, input().split())
    land = 1
    count = 0
    
    if w == 0 and h == 0:
        break

    test_map = [list(map(int, input().split())) for _ in range(h)]

    for i in range(0, h):  # 깊이우선탐색이기에 height
        for j in range(0, w):
            if test_map[i][j] == land:
                dfs(i, j)
                count += 1

    print(count)
