dr = [-1, 1, 0, 0]  # 디렉션인덱싱 행
dc = [0, 0, -1, 1]  # 디렉션인덱싱 열

# 1. 반복문으로 풀기
def Mz(N,maze):
    # 시작점을 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                si, sj = i, j

# 2. 재귀호출로 풀기
def dfs(r,c,visited):
    if Mz[r][c] == '3': # 목적지 도착
        return 1
    visited[r][c] = 1 # 방문여부 표시
    # 사방탐색 시작~~
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d] # nr, nc로 사방탐색 좌표 설정
        if 0 <= nr <N and 0<= nc < N and \
                Mz[nr][nc] != '1' and not visited[nr][nc]:
            if dfs(nr,nc,visited) ==1:
                return 1
    return 0 # 길을 못찾은 경우
    pass

# 3. while과 stack을 활용한 경우
def sol(si,sj):
    visited = [[0] * N for _ in range(N)]
    stack = [(si,sj)] # 경로를 저장하는 스택
    visited[si][sj] =1 # 방문여부 표시하는 비지티드
    # 경로탐색 시작~~
    while stack:
        r, c = stack[-1]
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            # 정상 범위 안에 있으면서, 통로거나 목적지이고
            # 방문하지 않았다면 >> 방문하겠다.
            if 0 <= nr < N and 0 <= nc < N and \
                    Mz[nr][nc] != '1' and not visited[nr][nc]:
                    # (nr, nc)를 경로에 추가
                    stack.append((nr,nc))
                    break
        else:
            stack.pop()

T = int(input())
for tc in range(1,1+T):
    N = int(input())
    maze = [list(map(int,input().split()))for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    print(f'#{tc} {Mz(N,maze)}')
    print(f'#{tc} {dfs(r,c,visited)}')

    # 통로는 0, 막혀있는 곳은 1, 시작지는 2, 도착지는 3