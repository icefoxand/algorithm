a = [] # 정렬 전 리스트
sorted_list = [] # 정렬된 데이터 리스트
cnt = [] # 각항목 갯수를 저장한 리스트

def counting_sort(list, s_list):
    cnt = [0] * (max(list) +1)
    for i in list:
        cnt[i] += 1
    for idx in range(1,len(cnt)):
		    cnt[idx] += cnt[idx-1]
	for j in range(len(list)-1, -1, -1):
		s_list[ cnt[ list[j] ] -1] = list[j]
		cnt [list[j]] -= 1

a= [2,0,1,2,3,0,2]
sorted_list = [0]*len(a)
counting_sort(a, sorted_list)
print(counting_sort(a,sorted_list))