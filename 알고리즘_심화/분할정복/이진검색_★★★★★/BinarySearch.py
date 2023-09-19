
arr = [2,4,7,9,11,19,23]
arr.sort()
# print(arr)
low = 0             # 찾는 범위의 가장 작은 값이 갖는 인덱스값
high = len(arr)-1   # 찾는 범위의 가장 큰 값이 갖는 인덱스값

## 반복문 버전
def binary_search_iter(target):
    while low <= high: # 데이터를 못찾은 경우에, 계속 검색을 한다
        mid = (low+high)//2
        # mid 값이 정답 자체인 경우 => mid를, 바로 정답으로 반환
        if arr[mid] == target:
            return mid
        # mid 값이 정답보다 작은 경우 => min 우측을 다시 검색범위로 지정
        elif arr[mid] < target:
            low = mid + 1
        # mid 값이 정답보다 큰 경우 => min 좌측을 다시 검색범위로 지정
        elif arr[mid] > target:
            high = mid - 1
    return "해당 target 데이터는 없습니다."

print(f'9 = {binary_search_iter(9)}')
print(f'10 = {binary_search_iter(10)}')

## 재귀호출 버전
def binary_search_recur(low, high, target):
    if low > high: # 기저조건: 언제까지 재귀호출을 반복할 것인가?
        return "해당 target 데이터는 없습니다"
    mid = (low+high)//2
    # mid 값이 정답 자체인 경우 => mid를, 바로 정답으로 반환. 즉 재귀를 안돌아도될 경우?
    if arr[mid] == target:
        return mid
    # mid 값이 정답보다 작은 경우 => min 우측을 다시 검색범위로 지정
    elif arr[mid] < target:
        return binary_search_recur(mid+1,high,target)
    # mid 값이 정답보다 큰 경우 => min 좌측을 다시 검색범위로 지정
    elif arr[mid] > target:
        return binary_search_recur(low,mid-1,target)
print(f'9 = {binary_search_recur(low,high,9)}')
print(f'10 = {binary_search_recur(low,high,10)}')