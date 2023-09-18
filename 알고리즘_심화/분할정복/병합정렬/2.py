# 병합정렬 실제 구현
# 인덱스 이동을 이용해서 merge_sort 구현
def merge_sort(arr,s,e):
    if s == e:    # 요소가 하나 > 정렬할 필요 없음
        return
    # arr = [1,3,7,10,4,5,6,8]
    # s = 0
    # e = len(arr)-1
    mid = (s + e) // 2
    # 절반을 각각 정렬한 상태여야 한다.
    merge_sort(arr,s,mid)
    merge_sort(arr,mid + 1,e)
    i = s
    j = mid + 1
    tmp = []
    while i <= mid and j <= e:
        # i랑 j랑 비교해서 더 작은 애를 복사하고
        # i또는 j를 증가 시키기
        if arr[i] < arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    # 남은 애들 갖다 붙이기
    while i <= mid:
        tmp.append(arr[i])
        i += 1
    while j <= e:
        tmp.append(arr[j])
        j += 1

    j = 0
    for i in range(s,e+1):
        arr[i] = tmp[j]
        j += 1


arr = [1,3,7,10,4,5,6,8]
merge_sort(arr,0,len(arr)-1)
print(arr)