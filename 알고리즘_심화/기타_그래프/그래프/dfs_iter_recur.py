graph = [
    [0,1,0,1,0],
    [1,0,1,1,1],
    [0,1,0,0,0],
    [1,1,0,0,1],
    [0,1,0,1,0]
]
adj_list = [
    [1,3],
    [0,2,3,4],
    [1],
    [0,1,4],
    [1,3]
]

adj_dict ={
    '0':[1,3],
    '1':[0,2,3,4],
    '2':[1],
    '3':[0,1,4],
    '4':[1,3],
}


visited = [0]*5
#### 반복 ####
def dfs_iter(s):
    visited = []
    stack = [s]

    # 가야할곳이 스택에 있는데, 스택이 비지않았다면 진행
    while stack:
        now = stack.pop()
        # 기방문 지점은 continue
        if now in visited:
            continue
        # 미방문 지점은 방문표시
        visited.append(now)
        # 킹능성 있는 곳들을 스택에 추가
        # for next in range(5)
        for next in range(4,-1,-1):
            # 미연결시 넘어가기
            if graph[now][next] == 0:
                continue # (팁: pass 조건을 이용해서 컨티뉴를 쓰기)

            # 기방문 지점은 스택에 미 추가
            if next in visited:
                continue

            stack.append(next)
    # 출력을 위한 반환
    return visited
print("dfs stack = ",end='')
print(*dfs_iter(0))
#### 재귀 ####

def dfs_recur(now):
    visited[now] = 1
    print(now, end=' ')

    for next in range(5):
        if graph[now][next] == 0:
            continue
        if visited[next]:
            continue

        dfs_recur(next)

print('dfs recur =', end=' ')
print(dfs_recur(0))

