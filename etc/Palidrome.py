def f(N,M,arr):
# 가로검사
    for i in range(N): # i: 0->9
        for j in range(N-M+1):
            for k in range(M//2):
                if arr[i][j+k] != arr[i][j+M-1-k]:
                    break
            else:
                result = []
                for t in range(j, j + M):
                    result.append(arr[i][t])
                return ''.join(result)
# 세로검사: 가로검사를 응용하면 됨.
    for i in range(N-M+1):
        for j in range(N):
            for k in range(M//2):
                if arr[i+k][j] != arr[i+M-1-k][j]:
                    break
            else:
                result = []
                for t in range(i, i + M):
                    result.append(arr[t][j])
                return ''.join(result)
T = int(input())
for tc in range(1,1+T):
    N, M = map(int, input().split()) # N*N arr. M길이의 회문.
    arr = [input() for _ in range(N)]
    print(f'#{tc} {f(N,M,arr)}')

    # 1. 대표주자(i,j)를 선정한다. 행우선순회로->열우선순회 순서로
    # 2. 대표가 돌면서 M길이의 회문이 있는지 체크한다.
    # 체크방법은 정석적인 반복문을 사용.
    # 대표는 arr의 특정행의 열에서 첨부터 끝까지 다 갈 필요가 없음에 유의. <- range 설정이 중요포인트
    # 3. 대표가 가로 세로로 각각 돈 후에 각 테케별로 성립한 팰린드럼의 형태를 반환.

    # reflection
    # 1. 의외로 시간이 많이 걸림. 왜냐면, j번째 열의 range 정할때 너무 귀납적으로 풀어서 그런듯. 연역적 논리 필요.
    # 더 나아가서는 빈출유형 풀이방법은 암기하는게 좋아보임.
    # 2. 해당하는 팰린드럼을 추출할때, 리스트 변환->join으로 합쳐서 꺼낼수 있고, 문자열 자체로 꺼낼수도 있음. 차이x.
    # else:
    # result = ''
    # for k in range(j, j + M):
    #     result += str(arr[i][k])
    # return result
    # 3. 7번째 줄에서 else를 바로 위 if와 같은줄에 위치시켰더니, 자꾸 테케3에서 오답떴음.
    # 해결: for문 돌리면서 break가 한번도 안걸렸을때는 for문과 같은 indentation 위치에 else를 써서, for-else문을 써야함!
    # 4. 19번째 줄에서 각 테케별로 팰린드럼이 1개씩만 존재하기 때문에 result를 초기화 가능.