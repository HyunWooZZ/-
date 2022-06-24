def solution():
    n = int(input())
    length = list(map(int ,input().split()))
    oilPrice = list(map(int ,input().split()))

    answer = 0
    cheap_oil = int(1e10)

    for i, price in enumerate(oilPrice):
        if i == n-1:
             break
    
        if price < cheap_oil:
            cheap_oil = price
        
        answer += cheap_oil * length[i]

    return answer

print(solution())

