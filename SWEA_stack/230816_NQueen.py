# 한 행에 하나의 퀸을 놓기
# 모든 행에 퀸을 다 높았다면, 해를 찾은것임
# N * N
N = 4
def f(row):
    global cnt
    if row == N: # 모든 행에 퀸을 놓은것임
        print('찾았습니다!')
        cnt += 1
        return
    for col in range(N): # row행의 모든 열에 퀸 놓아보기
        # (row,col)에 놓을수 있으면, 퀸 놓아보기
        if not col_check[col] and not dia_check1[row+col] and \
            not dia_check2[N-1 + (row - col)]:
            col_check[col] += 1
            dia_check1[(row + col)] += 1
            dia_check2[N - 1 + (row - col)] += 1
            f(row+1)
            col_check[col] -= 1
            dia_check1[(row + col)] -= 1
            dia_check2[N - 1 + (row - col)] -= 1

# 열 가능여부 표시 배열
col_check = [0] * N
# ↙ 대각선 가능여부 표시 배열
dia_check1 = [0] * (2 * N - 1)
# ↘ 대각선 가능여부 표시 배열
dia_check2 = [0] * (2 * N - 1)
cnt = 0

f(0)
print(cnt)