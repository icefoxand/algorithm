T = int(input())
for tc in range(1,1+T):
    N, M = map(int,input().split()) # 10 3
    num = list(map(int,input().split()))
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # N개의 숫자뭉치에서 M개의 이웃합을 구하고
    # 이웃합의 최대 최소의 차를 구하면 됨
    max_cnt = 0
    min_cnt = 10000*M

    for i in range(N-M+1):
        cntl =[]
        cnt = 0
        for j in range(M):
            cntl.append(num[i+j])
        for k in cntl:
            cnt += k

        if max_cnt < cnt:
            max_cnt = cnt

        if min_cnt > cnt:
            min_cnt = cnt
    print(max_cnt-min_cnt)
# print(f'1 :{cnt}')   # 132
#     print(f'2 :{cnt}') # 132
#         print(f'3 :{cnt}')
'''
        3 :6
        3 :15
        3 :27
        3 :42
        3 :60
        3 :81
        3 :105
        3 :132
        '''
            # print(f'4 :{cnt}')   # IndentationError : unexpected indent
            #     print(f'5 :{cnt}'  # IndentationError : unexpected indent