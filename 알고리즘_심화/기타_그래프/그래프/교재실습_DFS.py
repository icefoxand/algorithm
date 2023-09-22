data = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
V,E = 7,8
adj_mt = [[0]*(V+1) for _ in range(V+1)]
adj_ls = [[]for _ in range(V+1)]

for i in range(0,E*2,2):
    adj_mt[data[i]][data[i+1]] = 1
    adj_mt[data[i+1]][data[i]] = 1
    adj_ls[data[i]].append(data[i+1])
    adj_ls[data[i+1]].append(data[i])

# for row in adj_mt:
#     print(row)
# for row in adj_ls:
#     print(row)

def dfs(start):
    stack=[start]
    visited = [0]*(V+1)
    # visited[start] = 1

    while stack:
        current = stack.pop()
        if visited[current]:
            continue
        visited[current] = 1
        print(current,end=' ')
        for i in range(1,1+V):
            if adj_mt[current][i] and not visited[i]:
                stack.append(i)

dfs(1)
print()
# dfs(2)
print()
# bfs(1)
print()