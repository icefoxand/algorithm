def solution(sizes):
    answer = 0
    biggers = []
    smallers = []
    for i in range(len(sizes)):
        bigger = max(sizes[i])
        biggers.append(bigger)
        sizes[i].remove(bigger)
        smallers.append(sizes[i][0])
    # print(biggers)
    # print(sizes)
    # print(smallers)
    return max(biggers) * max(smallers)