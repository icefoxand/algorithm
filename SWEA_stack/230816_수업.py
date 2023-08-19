# def f(i,N):
#     if i == N:
#         print(bit, end=' ')
#         for j in range(N):
#             if bit[j]:
#                 print(A[j])
#                 return
#     else:
#         bit[i] = 1
#         f(i+1,N)
#         bit[i] = 0
#         f(i+1,N)
#         return
# A =[1,2,3]
# bit = [0]* 3
# f(0,3)
# 1부터 10까지 원소인 집합이 있을때, 부분집합의 합이 10인 경우는? 비트로 위치를 표시하라
# 강사님의 방법도 추가해서 정리하기.
def f(i,N,s,t):
    global cnt
    cnt += 1
    if s == t: # 정답 찾음
        print(bit)
        return
    elif i == N:
        return
    elif s > t: #가능성 없음
        return
    else:
        bit[i] = 1
        f(i+1,N,s+A[i],t)
        bit[i] = 0
        f(i+1,N,s,t)
N = 10
A = [i for i in range(1,N+1)] # 리컴 으로 만드는 경우도 잘 익히기
bit = [0]*N
cnt = 0
t =10
f(0,N,0,10)
print()
###
# def f(i,N):
#     if i == N:
#         print(A)
#     else:
#         for j in range(i, N):
#             A[i],A[j] = A[j], A[i]
#             f(i+1,N)
#             A[i],A[j] = A[j], A[i]
#
# A = [1,2,3]
# f(0,3)
### 중복순열 만드는 함수 <- 그림으로 한줄한줄 정확히 매칭 시켜보기
def perm(idx, used):
    if idx == N:
        print(perm_arr)
        return # 밑에 넘어가서 수행 하지말고 끝내라.
    for i in range(N):
        # 앞에서 썼던건 넣지말자
        if used[i] == 0: # 58번째 줄 if~ 이게 백트랙킹 임. 가볼필요 없는걸 걸러내는 역할
            perm_arr[idx] = arr[i]
            used[i] = 1
            perm(idx+1, used)
            used[i] = 0

def perm2(idx):
    if idx == N:
        print(arr)
        return
    for i in range(idx, N):
        arr[idx], arr[i] = arr[i], arr[idx]
        perm2(idx+1)
        arr[idx], arr[i] = arr[i], arr[idx]

arr = [1,2,3]
N = 3
perm_arr = [0] * N
used = [0] * N

perm(0,used)
print()
perm2(0)