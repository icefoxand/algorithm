# SWEA_파리퇴치
# 구미2반_최지원_작성
# ●구해야할것: 파리채를 내려쳤을때 잡는 파리수의 최댓값

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    N_data = [list(map(int,input().split()))for _ in range(N)]

    cnt_l = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            for q in range(M):
                for w in range(M):
                    cnt += N_data[i+q][j+w]
            cnt_l.append(cnt)
    max_ll = 0
    for cnt_ll in cnt_l:
        if max_ll < cnt_ll:
            max_ll = cnt_ll
    print(f'#{tc} {max_ll}')