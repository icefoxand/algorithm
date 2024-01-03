def solution(array):
    answer = []
    cnt = -1
    mx = max(array)
    for num in array:
        cnt += 1 
        if num == mx:
            idx = cnt
            # print(idx)
    answer.append(mx)
    answer.append(idx)
    return answer

print(solution([1,8,3]))