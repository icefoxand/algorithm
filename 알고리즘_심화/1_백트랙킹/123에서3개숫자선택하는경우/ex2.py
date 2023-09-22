# {1,2,3...10} 의 파워셋중 원소합이 10인 부분집합을 모두 출력하시오
arr = [i for i in range(1,1+10)]
print(*arr)
sum_arr = []
target =10
def bt(cnt):
    if sum_arr == target:
