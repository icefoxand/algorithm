# 주간3회1번_봉우리의갯수를찾아라!
# 유사문제: 풍선팡1,2 and 파리퇴치
# 나의 풀이
T = int(input())
for tc in range(1,1+T):
    N = int(input())
    data = [list(map(int,input().split()))for _ in range(N)]
    dir_idx=[[-1,0],[0,1],[1,0],[0,-1]] # 상우하좌
    cnt_bong_2 = 0
    for i in range(N):
        for j in range(N):
            h = data[i][j]
            cnt_bong_1 = 0 # 대표의 봉우리 가능성 테스트용 변수
            for k in range(4):
                ni = i + dir_idx[k][0]
                nj = j + dir_idx[k][1]
                if 0<= ni <N and 0<= nj <N and data[ni][nj]<h: # 만약 보조범위가 2차원배열 내부이고, 보조값이 대표값보다 작다면
                    cnt_bong_1 += 1
                    if (i,j) == (0,0) or (i,j) ==(0,N-1) or (i,j) ==(N-1,0) or (i,j) ==(N-1,N-1): # (그리고) 대표가 모서리 부분이라면
                        if cnt_bong_1 == 2:
                            cnt_bong_2 += 1
                    elif (i == 0 and j in range(1,N-1)) or (i == N-1 and j in range(1,N-1)) or (i in range(1,N-1) and j ==0) or (i in range(1,N-1) and j == N-1):
                        if cnt_bong_1 == 3:
                            cnt_bong_2 += 1
                    else:
                        if cnt_bong_1 == 4:
                            cnt_bong_2 += 1
    print(f'#{tc} {cnt_bong_2}')

# 효주의 풀이(flag variable)
def peak(N, arr):
    dr = [-1,0,1,0] # 상 우 하 좌
    dc = [0,1,0,-1]
    cnt = 0   # cnt : 봉우리 갯수. 조건을 만족하지 않는 경우 0 출력
    is_peak = True# 선택한 (r,c) 가 봉우리가 맞는지 검사
    for r in range(N):    # r : 행 순회
        for c in range(N):    # c : 열 순회
            for k in range(4):   # k : (r,c) 중심을 둔 네 방향 순회
                nr = r + dr[k]
                nc = c + dc[k]
                if 0<= nr <N and 0<= nc <N:
                    if arr[nr][nc] >= arr[r][c]:    # 여기 arr[nr][nc] - arr[r][c] 선언하면서 꼬임
                        is_peak = False
                        break
                    else:   # 모두 클 경우에만 is_peak = True
                        is_peak = True
            if is_peak:   # 순회 끝나고 만족할 경우에만 cnt up
                cnt += 1
    return cnt

# 문제1 봉우리 (배점 40)
T = int(input())
for tc in range(1, T + 1):
    N = int(input())   # N : 지도의 가로 세로 크기
    arr = [list(map(int, input().split())) for _ in range(N)] # h : 높이
    # print(arr) [[1, 1, 2, 1], [2, 1, 3, 1], [2, 1, 2, 1], [3, 4, 4, 4]]
    answer = peak(N, arr)
    print(f'#{tc} {answer}')  # answer : 봉우리 해당 지역 수, 없으면 0
