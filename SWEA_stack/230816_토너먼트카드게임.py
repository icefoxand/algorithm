# 유사문제: 거듭제곱
# 사용개념: 분할정복
def solve(start,end):
    m = (start+end)//2
    w1 = solve(start,m)
    w2 = solve(m+1, end)


T = int(input())
for tc in range (1,1+T):
    N = int(input())
