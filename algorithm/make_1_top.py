N = int(input())
d = [None] * 30001
def topdown(n: int, d: list[int]) -> int:
    if n == 1:
        d[1] = 0
        return d[1]
    else:
        ### 이미 계산되어 있는 경우
        if d[n] is not None:
            return d[n]
        ### 계산되어 있지 않은 경우
        else:
            answer = n
            if n % 2 == 0:
                answer = min(answer, topdown(n//2, d)+1)
            if n % 3 == 0:
                answer = min(answer, topdown(n//3, d)+1)
            if n % 5 == 0:
                answer = min(answer, topdown(n//5, d)+1)  
            d[n] = answer
            
            return d[n]
<<<<<<< HEAD
=======

>>>>>>> 8f3e7c960ce6f3a559d045b5c6fb0c3da4422656
print(topdown(N, d))

