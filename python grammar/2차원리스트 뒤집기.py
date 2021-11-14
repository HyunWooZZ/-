def solution(mylist):
    
    answer = list()
    
    for idx in range(len(mylist)):
        answer.append([])
        for i in mylist:
            answer[idx].append(i[idx])

    return answer





​mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_list = list(map(list, zip(*mylist)))


​





## 둘의 차이는 어마무시하다. 시간 복잡도 O(n^2)와 O(n)