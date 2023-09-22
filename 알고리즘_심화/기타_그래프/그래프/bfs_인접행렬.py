graph = [
    [0,1,0,1,0],
    [1,0,1,1,1],
    [0,1,0,0,0],
    [1,1,0,0,1],
    [0,1,0,1,0]
]

def bfs(s):
    visited = [0]*5

    queue = [s]
    visited[s] =1

    while queue:
        now =queue.pop(0)
        print(now, end=' ')

        for next in range(5):
            # 미연결시 넘어가기
            if graph[now][next] == 0:
                continue  # (팁: pass 조건을 이용해서 컨티뉴를 쓰기)

            # 기방문 지점은 스택에 미 추가
            if visited[next]:
                continue

            queue.append(next)
            visited[next]  =1

bfs(0)