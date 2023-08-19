# 중위표기식을 후위표기식으로 바꾸어 계산하는 프로그램

# def f1(str):
#
# def f2(str)
#
# T = 10
# for tc in range(1,1+T):
#     N = int(input())
#     str = input()
#     print(N, str)
#     # print(f'#{tc} {f(str)}')

# 3+4+5+6+7
# a@b => ab@ 이런식으로 사이에 있던 연산를 뒤로 빼는 방법
# 연산자는 + 뿐이며, 피연산자는 0~9인 정수만 주어짐

###
# 후위표기법으로 나타내진 수식을, 스택 이용하여 계산해내기!
# step3. 수식이 끝나면, 마지막으로 스택을 pop하여 출력.
def Cal_post(given):
    stack = [0] * 100
    top = -1
    for x in given:
        if x not in '+-/*':
            # step1-1. 피연산자를 만나면, 스택에 push.
            top += 1
            stack[top] = int(x)
            stack.append(x)
        else:
            # step1-2. 연산자를 만나면, 필요한 만큼의 피연산자를 스택에서 pop. 그 후, 연산결과를 다시 스택에 push.
            op1 = stack[top]
            top -= 1
            op2 = stack[top]
            top -= 1
            if x == '+':
                top += 1
                stack[top] = op2 + op1
                stack.append(op2+op1)
            elif x == '-':
                top += 1
                stack[top] = op2 - op1
                stack.append(op2 - op1)
            elif x == '/':
                top += 1
                stack[top] = op2 // op1
                stack.append(op2 // op1)
            elif x == '*':
                top += 1
                stack[top] = op2 * op1
                stack.append(op2 * op1)

    return stack.pop()

given1 = '6528-*2/+'
print(Cal_post(given1))

###
# def Cal_post2(s):
#     stack = [0] * 100
#     top = -1
#     for x in s:
#         if x not in '+-/*': # 피연산자면 stack 에 push
#             top += 1
#             stack[top] = int(x)
#         else:
#             op2 = stack[top]  # pop()
#             top -= 1
#             op1 = stack[top]  # pop()
#             top -= 1
#             if x == '+':  # op1 + op2 (먼저 꺼낸 게 오른쪽으로)
#                 top += 1
#                 stack[top] = op1 + op2
#             elif x == '-':
#                 top += 1
#                 stack[top] = op1 - op2
#             elif x == '/':
#                 top += 1
#                 stack[top] = op1 // op2
#             elif x == '*':
#                 top += 1
#                 stack[top] = op1 * op2
#
#     return stack[top]
# s1 = '6528-*2/+'
# print(Cal_post2(s1))

###

# step1. 피연산자 vs 연산자
# step2. 피연산자 -> 출력
#        연산자 -> 우선순위에 따라 스택에 넣거나 출력
# step3. stack[top]의 연산자 보다 우선순위 높으면, 그냥 넣기
# step4. 만약 stack[-1]의 우선순위 보다 c의 우선순위 높으면: stack.append(c)

def Cal_change(exp): # 중위식 -> 후위식으로 변경해주는 계산기
    N = len(exp)
    post_exp = ''
    stack = []
    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}
    for c in exp: # ( 6 + 5 * ( 2 - 8 ) / 2
        if c in '+-*/()': # 연산자
            if c == ')': # 닫괄 나오면,
                         # 여괄 만날때까지 모조리 pop() 반복
                while stack[-1] != '(': # 여괄 만나기 전이면,
                    post_exp += stack.pop()
                stack.pop() # 여괄을 만나면 팝()
                continue    # 다음토큰 읽어오기(for c in exp: <-이때로 감)
            if not stack:                 # 스택이 비어있다면~?
                stack.append(c)
            elif isp[stack[-1]] < icp[c]: # 스택이 안 비어있다면~?
                stack.append(c)
            else: # 같거나 높으면... 스택 안에 다뺄것!
                  # 나보다 우선순위 낮은애가 stack에 있으면?
                  # 내가 들어간다.
                  # 나보다 낮은애가 top이 될때까지~
                while stack and isp[stack[-1]] >= icp[c]:
                    post_exp += stack.pop()
                stack.append(c)
        else: # 피연산자
            post_exp += c
    while stack: # 스택에 남아있는 연산자들 출력
        post_exp += stack.pop()
    return post_exp

exp1 = '(6+5*(2-8)/2)'
print(Cal_change(exp1))
####
