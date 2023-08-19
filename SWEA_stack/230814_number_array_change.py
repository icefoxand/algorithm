# 그림을 그려서 살펴보기
# (r,c) -> (c,N-1-r)
# rotate():원본 받아서 90도 회전한 배열을 반환하는 함수
def rotate(origin):
    new_mat = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            new_mat[c][N-1-r] = origin[r][c]
    for i in range(N):
        new_mat[i]
    return new_mat

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [input().split() for _ in range(N)]
    matrix90 = rotate(matrix)
    matrix180= rotate(matrix90)
    matrix270= rotate(matrix180)
    # 위처럼 같은 내용물로 여러개가 나오면 줄을 맞춰주는게 보기좋다.
    print(f'#{tc} {rotate(matrix)}')


