# 행/열 우선순회하면서 유물이 나타나면
# 테케 별로 가장 긴 구조물의 길이를 찾는 프로그램을 찾아라
# def f(N,M,data):
#     max_cnt = 0
#
#     for i in range(M+1):
#         # 하나의 열 검사
#         cnt = 0
#         for j in range(N+1):
#             if data[j][i] == 1:
#                 cnt += 1
#             else:
#                 if max_cnt < cnt:
#                     max_cnt = cnt
#                 cnt = 0
#
#     for j in range(N+1):
#         # 하나의 행 검사
#         cnt = 0
#         for i in range(M+1):
#             if data[i][j] == 1:
#                 cnt += 1
#             else:
#                 if max_cnt < cnt:
#                     max_cnt = cnt
#                 cnt = 0
#     return max_cnt

T = int(input())
for tc in range(1,1+T):
    N, M = map(int, input().split())
    data = [list(map(int, input().split()))+[0] for _ in range(N)]
    data.append([0]*(M+1))
    # Q.하단/우단을 0으로 감싸는건 왜 하는건가?
    # 아마도 OOR(out of range) 문제 해결하려고?

    print(data)
    # [[0, 1, 0, 0],
    # [0, 1, 0, 0],
    # [0, 1, 0, 0],
    # [0, 0, 0, 0]]
    # print(f'#{tc} {f(N,M,data)}')

# input.txt
# 3
# 3 3
# 0 1 0
# 0 1 0
# 0 1 0
# 3 3
# 0 1 0
# 1 1 1
# 0 0 0
# 8 8
# 1 0 0 0 0 0 1 0
# 1 0 1 1 1 0 1 0
# 1 0 0 0 0 0 1 0
# 0 0 0 1 0 0 1 0
# 0 0 0 1 0 0 1 0
# 0 1 1 0 0 0 1 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 1 1 1 1

# output.txt
# #1 3
# #2 3
# #3 6