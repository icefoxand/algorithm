def solution(num_list, n):
    answer = []
    for a in range(0,len(num_list),n):
        answer.append(num_list[a:a+n])
    return answer

num_list0, n0 = [1, 2, 3, 4, 5, 6, 7, 8], 2

print(solution(num_list0, n0))

# list01.py와 거의 동일 하다. answer 구조를 아예 고치지 않고 푸는 방법이 있나?
