def binary_search_iter(A,target):
    # 1) A라는 정렬된 리스트에
    # 2) target 이라는 수가 들어있는지? 방향이 바뀌어가며 위치 하는가?
    global cnt
    start = 0
    end = N-1
    dir = 0 # 0은 탐색시작, 1은 왼,,2는 오
    while start <= end:
        mid = (start + end)//2
        if A[mid] == target:
            cnt +=1
            return True
        elif A[mid] < target: # 이전에 오른쪽 아니었다면, 오른쪽 봐야함
            if dir ==2:
                break
            dir = 2
            start = mid +1
        elif A[mid] > target: # 이전에 왼쪽 아니었다면, 왼쪽을 봐야함
            if dir ==1:
                break
            dir = 1
            end = mid -1
    return False

T = int(input())
for tc in range(1,1+T):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()  # [1,3,5,7,9]
    B.sort()  # [1,2,3,4,5]
    cnt = 0

    for i in B:
        binary_search_iter(A,i)

    print(f'#{tc} {cnt}')