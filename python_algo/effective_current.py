#### 방법론 ####
# 먼저 갖고 있는 화폐들을 저장
# 갖고 있는 화폐들을 차근차근 넣어가며 비교할 텐데
# 해당 화폐에서 하나를 뺀 것이 기존 메모한 곳에 있는 경우 거기에서 1 더한 것과 현재 저장된 것과 작은 것을 선택
# 따라서 일반화 하면 다음과 같다
# 금액 i를 만들 수 있는 최소한의 화폐 개수를 a_i라고 할 때, 화폐의 단위를 k라고 할 때
# a_(i-k)는 금액 i-k를 만들 수 있는 최소한의 화폐 갯수를 의미한다고 할 때
# dp[i] = min(d[i], d[i-k] + 1) 

def effectiveCurrency():
    answer = -1
    n, m = map(int, input().split())
    # 화폐종류 받기
    array = []
    dp = [10001] * (m + 1)
    dp[0] = 0
    for _ in range(n):
        array.append(int(input()))

    for i in array:
        for j in range(i, m + 1):
            dp[j] = min(dp[j], dp[j-i] + 1)

    if dp[m] != 10001:
        answer = dp[m]
    
    return answer

print(effectiveCurrency())
    
    



 