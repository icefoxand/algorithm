# https://www.acmicpc.net/problem/1647 관련 백준문제
# https://doing7.tistory.com/82 관련 블로그 설명
# 0 ~ 9
# make set: 집합을 만드는 과정
parent = [i for i in range(10)]
print(parent)

# union:
def find_set(x):
    if parent[x] == x:
        return x
    # return find_set(parent[x])

    # 경로압축
    parent[x] = find_set(parent[x])
    return parent[x]
# find:
def union(x,y):
    # 1. 이미 같은 집합인지 체크
    # 2. 다른 집합 이라면, 같은 대표자로 수정함
    x = find_set(x)
    y = find_set(y)

    # 대표자가 같은경우
    if x == y:
        print("사이클 발생")
        return
    # 대표자가 다른경우: 같은 대표자로 수정
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


union(0,1)
union(2,3)
union(1,3)
# 이렇게 추가하면 싸이클이 발생함: 이미 동집합에 속해있는 원소를 한번더 집합으로...
union(0,2)

# 같은 그룹인지 판별
t_x = 0
t_y = 2

if find_set(t_x) == find_set(t_y):
    print(f'{t_x}와 {t_y}는 같은 집합에 속해 있습니다.')
else:
    print(f'{t_x}와 {t_y}는 다른 집합에 속해 있습니다.')
