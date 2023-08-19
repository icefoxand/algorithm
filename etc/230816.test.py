lst = [1,2,3,4,5]
'''
lst[0]+lst[1]+lst[2]
lst[1]+lst[2]+lst[3]
lst[2]+lst[3]+lst[4]
'''
max_num =0
for i in range(3):
    l =[]
    num = 0
    for j in range(3):
        l.append(lst[i+j])

    for number in l:
        num += number

    if max_num < num:
        max_num = num
print(max_num)