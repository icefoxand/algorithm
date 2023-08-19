# 2023.08.02_SWEA_풍선팡1 (더 어려운 버전)
# 구미2반_최지원_작성
#
# ●구해야할것: NxM개의 풍선에 들어있는 종이 꽃가루 개수 A가 주어지면, 한 개의 풍선을 선택해 터뜨렸을 때 날릴 수 있는ㄴ 꽃가루 수 중 최대값을 출력하는 프로그램을 만드시오.
# (3<=N, M<=100)

T = int(input())
for tc in range(1,1+T):
    N,M = map(int,input().split())
    # 리스트가 반복되는 범위는 행의 갯수이므로, M이 아니라 N이다.(아까 혼동!)
    data = [list(map(int,input().split())) for _ in range(N)]
    # print(N,M) # 입력 디버깅
    # print(data) # 입력 디버깅
    dir_idx= [[-1,0],[0,1],[1,0],[0,-1]] # 디렉션인덱싱으로 '상우하좌' 쪽으로 움직일수 있는 좌표 쌍들을 리스트로 만듦
    cnt_l = [] # 각 대표주자(이하'대표')들의 총 꽃가루 합(이하'값')들을, 담을 cnt_l 변수를 빈 리스트로 선언
    result =0 # 결과를 담을 result 변수를 인트로 선언
    # data[i][j]: 대표의 값, data[i][j+k]: 대표의 상우하좌를 돌고 있을 보조주자(이하 '보조')들의 값
    for i in range(N): # N개의 행을 반복할 i
        for j in range(M): # M개의 열을 반복할 j
            cnt = 0 # 대표와 그 주변 보조들의 값을 모두 더해줄 cnt 변수를 0으로 선언함
            repre = data[i][j] # 대표의 값을 repre 라는 변수에 저장해준다
            cnt += data[i][j] # (대표의 좌표가 먼저 나오므로,) cnt에 더해준다.
            for k in range(4): # ni=i+(-1,0,1,0), nj=j+(0,1,0,-1) 로, 보조가 '상우하좌'를 돌게하는 반복문 시작
                for r in range(1, repre+1): # 1부터 repre 까지의 수를 r로 반복한다
                    ni = i+(dir_idx[k][0])*r # 보조들의 행 좌표(보조 풍선이 상우하좌로 1부터 r만큼 더 터짐)
                    nj = j+(dir_idx[k][1])*r # 보조들의 열 좌표(보조 풍선이 상우하좌로 1부터 r만큼 더 터짐)
                    if 0<= ni <N and 0<= nj <M: # 주어진 N*M 좌표 내에서 보조가 돌게한다
                        cnt += data[ni][nj] # 보조들의 값을 cnt에 담는다
            cnt_l.append(cnt) # '상우하좌'를 모두 돈 다음 최종 cnt값을 cnt_l에 한개씩 담는다
    max_ll =0 # cnt_l의 최댓값을 구하기위해, 최댓값 변수를 0으로 선언한다
    for cnt_ll in cnt_l: # cnt_l 속의 원소들을 하나씩 cnt_ll로 꺼낸다
        if max_ll < cnt_ll: # 최댓값 변수보다 cnt_ll이 크다면
            max_ll = cnt_ll # cnt _ll을 최댓값 변수로 갱신한다.
    result = max_ll # 최댓값을 result 변수에 담아, 출력을 준비한다.

    print(f'#{tc} {result}') # 결과를 원하는 바에 맞게 출력한다.