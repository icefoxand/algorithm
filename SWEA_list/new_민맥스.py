# SWEA_MinMAx
# 구미2반_최지원_작성

# ●구해야 할 것: 주어진 수 배열의 최댓값과 최솟값을 찾아내서 그 차를 출력하기

T = int(input()) # 테스트케이스의 수를 입력 받는다. 입력받은 직후는 스트링이므로, 인트(정수)로 변경해준다.
for tc in range(1,1+T): # 1부터 T까지 하나씩 나오는 tc를 포 반복문으로 돌린다
    N = int(input())  # 숫자 배열의 갯수 N을 입력받는다.
    numbers = list(map(int,input().split())) # 입력 받을 배열의 정수들이 공백으로 띄어져 있으므로, 스플릿 메써드를 사용하여 입력받고 정수화 한후 리스트로 묶어준다
    # print(N, numbers) # 입력 디버깅
    max_n = 0 # 추후 numbers 리스트 안에서 원소를 하나씩 꺼내서 max_n과 비교하여 최댓값을 갱신할 예정이므로, max_n을 정수로 선언한다. 모든 numbers의 원소를 돌때 까지 계속 존재해야 하므로, 11번줄 for문 보다 위 라인에 써준다.
    min_n = 1000000 # 위와 마찬가지 방법으로 최솟값을 갱신할 예정이므로, min_n을 정수로 선언해준다. 1000000을 할당해주는 이유는, 입력받는 배열의 정수의 최댓값이 100만 이기 때문이다.

    for number in numbers: # 입력받은 numbers 리스트에서 원소를 하나씩 꺼내기를 반복한다
        if max_n < number: # 만약 number가 max_n 보다 크다면?
            max_n = number # 최댓값을 number로 갱신한다
        if min_n > number: # 만약 number가 min_n 보다 작다면?
            min_n = number # 최솟값을 number로 갱신한다

    # print(max_n) # 출력 중간 디버깅
    # print(min_n) # 출력 중간 디버깅
    print(f'#{tc} {max_n-min_n}') # 결과를 출력한다
