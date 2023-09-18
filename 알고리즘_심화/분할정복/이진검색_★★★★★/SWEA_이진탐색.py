def binary_search_iter(A0,target):
    # 1) A0라는 정렬된 리스트에
    # 2) target 이라는 수가 들어있는지?
    global l, h, cnt
    while l <= h:
        mid = (l+h)//2
        if A0[mid] == target:
            cnt += 1
            return A0[mid]
        elif A0[mid] < target:
            l = mid +1
        elif A0[mid] > target:
            h = mid -1
    return

T = int(input())
for tc in range(1,1+T):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort() # [1,3,5,7,9]
    B = list(map(int,input().split()))
    B.sort() # [1,2,3,4,5]

    # print(N,M,A,B)
    # print()
    l, h = 0, N-1 # 탐색구간의 시작 인덱스, 끝 인덱스
    cnt = 0

    for i in B:
        print(binary_search_iter(A,i))

    print(f'#{tc} {cnt}')