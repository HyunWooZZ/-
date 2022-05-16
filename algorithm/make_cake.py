
n, m = map(int, input().split())
cake = list(map(int, input().split()))

def cut_cake(cake: list[int], m: int) -> int:
    start = 0
    end = max(cake)

    while start <= end:
        sum_cake = 0
        mid = (start + end) // 2
        print(mid)
        for i in cake:
            if i > mid:
                sum_cake += i - mid
        
        else:
            if sum_cake < m: # 자르는 높이가 높은 경우
                end = mid - 1
            else:
                answer = mid
                start = mid + 1 # 자르는 높이가 낮은 경우

    else:
        return answer




print(cut_cake(cake, m))






