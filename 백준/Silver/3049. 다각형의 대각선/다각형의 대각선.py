def combination_count(n, k):
    if n < 0 or k < 0 or k > n:
        return 0  # 조합이 불가능한 경우 0 반환

    # 이항 계수를 계산하여 조합의 수를 반환
    result = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        result *= (n - i)
        result //= (i + 1)

    return result

# 예제 사용
n = int(input())
print(combination_count(n,4))