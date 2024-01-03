def solution(my_str, n):
    answer = []
    # step1. 잘라냈을때 첫번째에 올 str를 끊어낸다
    for first in range(0,len(my_str),n):
        # step2. 해당 순환에 속하는 첫 str ~ 끝 str 까지를 빈 []에 추가한다.
        answer.append(my_str[first:first+n])
        
    return answer

my_str0, n0 = "abc1Addfggg4556b", 6

print(solution(my_str0, n0))