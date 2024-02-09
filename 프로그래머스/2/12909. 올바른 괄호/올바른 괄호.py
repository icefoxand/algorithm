def solution(s):
    empty = []
    for br in s:
        if br == "(": # 여는 괄호라면?
            empty.append(br) # empty에 넣는다
        elif br == ")": # 닫는 괄호라면?
            if not empty: # 만약 empty에 여는 괄호가 없어서 비어있다면?
                return False
            else:
                empty.pop()
    
    return not empty