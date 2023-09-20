# 각 노드마다 갈 수 있는 지점의 개수가 다르므로 range 쓸 때 index 조심

graph = [
    [1, 3],
    [0, 2, 3, 4],
    [1],
    [0, 1, 4],
    [1, 3]
]


# DFS
# stack 버전

def dfs_stack(start):
    visited = []
    stack = [start]

    while stack:
        now = stack.pop()
        # 이미 방문한 지점이라면 continue
        if now in visited:
            continue

        # 방문하지 않은 지점이라면, 방문 표시
        visited.append(now)

        # 갈 수 있는 곳들을 stack 에 추가
        # for next in range(5):
        # 작은 번호부터 조회
        for to in range(len(graph[now]) - 1, -1, -1):
            # 연결이 안되어 있다면 있다는 건 애초에 저장하지 않았으므로 체크할 필요가 없음
            # if graph[now][next] == 0:
            #     continue

            next = graph[now][to]

            # 방문한 지점이라면 stack에 추가하지 않음
            if next in visited:
                continue

            stack.append(next)

    # 출력을 위한 반환
    return visited


print('dfs stack =', end=' ')
print(*dfs_stack(0))

# DFS - 재귀
# MAP 크기(길이)를 알 때 append 형식말고 아래와 같이 사용하면 훨씬 빠르다
visited = [0] * 5


def dfs_recur(now):
    visited[now] = 1
    print(now, end=' ')
    for to in range(len(graph[now])):
        next = graph[now][to]

        # 연결이 안되어 있다면 있다는 건 애초에 저장하지 않았으므로 체크할 필요가 없음
        # if graph[now][next] == 0:
        #     continue

        if visited[next]:
            continue
        dfs_recur(next)


print('dfs recur =', end=' ')
dfs_recur(0)
print()