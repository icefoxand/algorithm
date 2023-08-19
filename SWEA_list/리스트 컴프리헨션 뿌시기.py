ll = []
for i in range(5):
    l =[]
    for j in range(5):
        l.append(j)
    ll.append(l)

print(ll)
print()
# 위의 ll을 컴프리헨션으로 만들어보기
lll = [[j for j in range(5)]for i in range(5)]

print(lll)
print()

llll = [j for j in range(5)for i in range(5)]
print(llll)