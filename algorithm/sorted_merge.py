def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    # 홀수 or 짝수
    # 홀수면 센터값
        # 짝수면 반가리
        # 정렬되어 있다. 그러면 해당 수열을 합치고, 길이에 따라 해당 값을 다르게 리턴하자
    from collections import deque 
    nums1 = deque(nums1)
    nums2 = deque(nums2)
    num_list = []

    while nums1 or nums2:       
        # 둘다 들어있는 경우
        if nums1 and nums2:
            if nums1[0] >= nums2[0]:
                num_list.append(nums2.popleft())
            else:
                num_list.append(nums1.popleft())
            continue
        
        # nums1만 들어있는 경우
        elif nums1:
            num_list.append(nums1.popleft())
            continue
         # nums2만 들어있는 경우
        else:
            num_list.append(nums2.popleft())
            continue
    
    if len(num_list) == 1:
        return num_list[0]

    if len(num_list) % 2 == 1:
        return float(num_list[len(num_list) // 2])
    
    else:
        return (num_list[len(num_list)//2 - 1] + num_list[len(num_list) // 2]) / 2

print(findMedianSortedArrays(nums1=[1, 3], nums2=[2]))