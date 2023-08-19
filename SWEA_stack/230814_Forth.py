def Cal_post(given):
    stack = [0] * 100
    top = -1
    for x in given:
        if x not in '+-/*.':
# 피연산자를 만나면,
# 스택에 push.
            top += 1
            stack[top] = int(x)
            stack.append(x)
        else:
# 연산자를 만나면,
# 필요한 만큼의 피연산자를 스택에서 pop. 그 후, 연산결과를 다시 스택에 push.
            if len(stack) >= 2:
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

T = int(input())
for tc in range(1,1+T):
    exp1 = input().split()
    print(f'#{tc} {Cal_post(exp1)}')
# 에러처리를 어떻게 할지..이게 제일 문제임.
