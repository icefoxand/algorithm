# SWEA_연속된1의갯수
# 구미2반_최지원_작성
# ●구해야할것: 1과 0으로 이루어진 배열에서, 연속된 1의 갯수 중 최댓값은?

T = int(input()) # 3
for tc in range(1,1+T): # 1,2,3
    N = int(input()) # 10
    numbers = list(map(int,input())) # [0,0,1,1,0,0,1,1,1,0]
    # print(N, numbers) # 입력 확인 디버깅
    # print()
    cnt_l = []
    cnt = 0
    for i in range(N): # i:0->9
        if numbers[i] == 1:
            cnt += 1
            if i == N-1:
                cnt_l.append(cnt)
                break
        else:
            if cnt != 0:
                cnt_l.append(cnt)
            cnt = 0
    max_cnt = 0
    for cnt_ll in cnt_l:
        if max_cnt < cnt_ll:
            max_cnt = cnt_ll
    print(f'#{tc} {max_cnt}')