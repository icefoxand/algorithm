def f(word_short,word_long):
    result =0
    l_long,l_short = list(word_long), list(word_short)
    len_long,len_short = len(l_long), len(l_short)
    for i in range(len_long-len_short+1):
        word = ''
        for j in range(len_short):
            word += l_long[i+j]
        if word == word_short:
            result = 1
            break
    return result

T = int(input())
for tc in range(1,1+T):
    word_short = input()
    word_long = input()
    print(f'#{tc} {f(word_short,word_long)}')

    # reflection
    # 1. 한편, 함수를 이런 방식으로 꾸밀수도 있음.
    # if word_target.count(word_pattern) != 0:
    #     return 1
    # return 0