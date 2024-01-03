def solution(array):
    answer = 0
    for li in array:
        # 주의해야 할 점: str(li) : true, "li" : false
        for one in str(li):
            if one == '7':
                answer += 1
    
    return answer

print(solution([7, 77, 17]))