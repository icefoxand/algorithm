def f(word):
    result=''
    if len(word)>=3:
        if word == word[::-1]:
            return 1
        else:
            return 0
# 다른방법1
# def f(word):
#     s = list(word) # ['l','e','v','e','l']
#     N = len(s)
#     for w in range(0,N//2):
#         if s[w] != s[N -1-w]:
#             return 0
#         else:
#             return 1

T = int(input())
for tc in range(1,1+T):
    word = input()

    print(f'#{tc} {f(word)}')

    # reflection
    # 1. 다른방법을 찾아보았고, 잘 작동함.