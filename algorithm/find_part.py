from bisect import bisect_left
import sys

N = int(input())
remain = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(input())
request = list(map(int, sys.stdin.readline().rstrip().split()))


def binarySearch(array, target, start, end):
    if start > end:
        return None
    else:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        
        elif array[mid] > target:
            return binarySearch(array, target, start, mid-1)
        
        else:
            return binarySearch(array, target, mid+1, end)

def find_part(remain: list[int], request: list[int]) -> list[bool]:
    answer = []
    remain.sort()
    for i in request:
        temp = binarySearch(remain, i, 0, len(remain))
        if temp is not None:
            answer.append("yes")
        else:
            answer.append("no")
    return answer

print(find_part(remain, request))


######################
####counting sort#####
######################

n = int(input())
array = [0] * 1000001
for i in input.split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')

    else:
        print('no', end=" ")

##################
#####set 자료형 ####
#################3


N = int(input())
remain = set(map(int, sys.stdin.readline().rstrip().split()))

M = int(input())
request = list(map(int, sys.stdin.readline().rstrip().split()))
def find_part(remain, request):
    answer = []
    for i in request:
        if i in remain:
            answer.append('yes')

        else:
            answer.append('no')
