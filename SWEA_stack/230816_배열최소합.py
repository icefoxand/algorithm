# 유사문제: N-Queen, 순열문제
# 사용개념: 백트랙킹, 재귀호출
def f(N,data):
    if i in range(N):
        if i == N-1:
            pass
        for j in range(N):
            data[i][j]

    # 노드가 진행될때,
    # 현재 노드의 행이 N과 같다면? 끝
    # 현재 노드의 행이 N이 아니라면? 미완성
        # 다음 행으로 넘어가는 깊이탐색 수행
        # 방문중인 노드는 유망한가?
            # 유망하다면?
                # 선정 다음행으로
            # 유망하지 않다면?
                # 백트랙킹
T = int(input())
for tc in range(1,1+T):
    N = int(input())
    data = [list(map(int,input().split()))for _ in range(N)]
    j_check = [0] * N
    print(data)
    # print(f'#{tc} {f(N,data)}')
# 방문장소를 체크해줄 리스트 한개 필요
# 방문하면 1으로 표시시
# 방문전이면 0으 표시
# 조건이 모두 만족하면, 재귀가 끝나게
#


# 3
# 3
# 2 1 2
# 5 8 5
# 7 2 2
# 3
# 9 4 7
# 8 6 5
# 5 3 7
# 5
# 5 2 1 1 9
# 3 3 8 3 1
# 9 2 8 8 6
# 1 5 7 8 3
# 5 5 4 6 8