# {1,2,3}집합에서 3개 숫자를 선택하는 기본적인 예제
# 이미사용한 숫자는 사용하지 않도록 한다.
arr = [i for i in range(1,1+3)] # [1,2,3]
path = [0]*3                    # [0,0,0]
def back_tracking(cnt):
    # 중요)))재귀를 끝내는 기저조건: 숫자3개 고르면 종료
    if cnt == 3:
        print(*path)
        return
    # (추가적인) 가지치기

    # 반복문
    for num in arr:             # [1,2,3]
        # 중요)))중심 가지치기: 중복된 숫자제거
        if num in path:
            continue
        # 중요)))돌기 전 로직
        path[cnt] = num
        # 다음재귀 함수 호출
        back_tracking(cnt+1)
        # 중요)))돌아와서 할 로직: 왜하나? 전단계로 왔을때 초기화 필요.
        path[cnt] = 0
# 재귀함수를 호출하여,, 함수를 작동시킨다.
back_tracking(0)