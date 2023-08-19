def f(N,M,arr):
    max_total =0
    dir_idx = [[-1,0],[0,1],[1,0],[0,-1]] #
    for i in range(N):
        for j in range(M):
            total = 0
            now = arr[i][j]
            total += now
            for k in range(4):
                for l in range(1,now+1):
                    if 0<= i+(dir_idx[k][0]*l)<N and 0<= j+(dir_idx[k][1]*l)<M:
                        total += arr[i+(dir_idx[k][0]*l)][j+(dir_idx[k][1]*l)]
                        if max_total < total:
                            max_total = total
    return max_total
T = int(input())
for tc in range(1,1+T):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split()))for _ in range(N)]
    # print(N,M,arr)
    print(f'#{tc} {f(N,M,arr)}')

    # reflection
    # 1. in dir_idx, 0, -1 이렇게 써야하는데 쉼표를 안쓰고 0-1 일케 써서, OOR(out of range)나옴
    # 2. in def, return으로 결괏값 반환을 안하고 print로 끝냈더니, 제대로 아웃풋을 써도 None뜸
    # 3. in dir_idx, [[상],[우],[하],[좌]] 이런식으로 쓰는 개선을 적용했더니 조금더 보기 편해짐.
    # 4. 문제요건중, 대표주자의 값만큼  상우하좌로 더 많이 가야하는걸 구현할때 곱하기를 써야하는걸 찾아내는게 살짝 힘들었음.
    # 종이에 꼭 작은 케이스를 써보면서 생각해보기. 급하게 머리로만 하려고 하면 ㄴㄴ. 마치 암산같은 느낌이라서 잘 안풀림.