# BruteForce. 고지식한_패턴검색_알고리즘.
def BF(p,t):
    M = len(p)  # 2
    N = len(t)  # 4
    i = 0 # t 금광의 인덱스
    j = 0 # p 금의 인덱스
    while i < N and j < M: # 멈추기전에 언제까지 돌아야 하는지를 보통 조건으로 줌
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == M : return i-M # 검색 성공
    else: return -1 # 검색 실패
p1 = 'BC' # 찾아야 할 (짧은) 패턴. 금?
t1 = 'ABCD' # 전체 텍스트. 금광?
print(BF(p1,t1))
# BF의 시간복잡도: 최악의경우, O(M*N). 비교횟수를 줄일수 있는 방법?
# KMP 알고리즘
# 보이어-무어 알고리즘: 대부분의 상용sw에서 채택. 금:왼쪽<-오른쪽

