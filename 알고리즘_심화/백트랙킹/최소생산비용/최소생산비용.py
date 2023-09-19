# 목표: 깊이우선탐색 + 백트랙킹

def dfs(idx,sum_data):
    global ans
    if sum_data >= ans:
        return
    if idx == N:
        ans = sum_data

    for i in range(N): # 0 1 2
        if not visited[i]: # 방문전이라면
            visited[i] = 1 # 방문하고 1으로 채우고
            dfs(idx+1,sum_data + data[idx][i]) # 재귀호출하고
            visited[i] = 0 # 돌아오면 0으로 초기화

T = int(input())
for tc in range(1,1+T):
    N = int(input())
    data = [list(map(int,input().split()))for _ in range(N)]
    # print(N, data)
    visited = [0 for _ in range(N)] # 기본적으로 1로 채움
    # print(visited)
    ans = 0xfffff
    dfs(0,0)
    print(f'#{tc} {ans}')
