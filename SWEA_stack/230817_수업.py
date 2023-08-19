def enQ(data):
    global rear
    if rear == Qsize -1: # 가득 차있다면
        print('Q is full')
    else: # 가득 안 찼다면
        rear += 1
        Q[rear] = data

def deQ():
    global front
    if front == rear: # 비어있다면
        print('Q is empty')
    else: # 비어있지 않다면
        front += 1
        return Q[front]

Qsize = 3
Q = [0] * Qsize
rear = -1
front = -1
#####
enQ(1)
enQ(2)
rear += 1
Q[rear] =3
#####
# while front != rear: # 큐가 비어있지 않다면
#     front += 1
#     print(Q[front])
#
#####
# enQ(4)
print(deQ())
print(deQ())
print(deQ())
###########################################################################
#cQ 관련

def enQ(data):
    global rear
    if (rear+1) % cQsize == front:
        print('cQ is Full')
    else:
        rear = (rear+1) % cQsize
        cQ[rear] = data

def deQ():
    global front
    front = (front+1) % cQsize
    return cQ[front]

cQsize =4
cQ = [0]* cQsize
front =0
rear =0

enQ(1)
enQ(2)
enQ(3)
# print(deQ())
# print(deQ())
# print(deQ())
enQ(4)