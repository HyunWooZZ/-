def solution(phone_book):
    
    phone = {phone_num: len(phone_num) for phone_num in phone_book}

    for i in phone:
        phone_ls = [num for num in phone if num[:len(i)] == i]
            
        if len(phone_ls) > 1:
            return False
    
    else:
        return True
"""
위의 시간 복잡도는 O(N^2) 이다. 
"""



    
def solution(phone_book):
    for l in range(1, 21):
        
        pre = {pb for pb in phone_book if len(pb) == l}
        compare = {pb[:l] for pb in phone_book if len(pb) > l}
        if pre & compare:
            return False
    return True

"""
위의 시간 복잡도는 O(N^2)처럼 보이지만 O(N)이다.
첫번째 for 문이 상수로 고정되어 있기 때문. 

언뜻 보면 코드의 의도는 비슷해 보이지만, 결과는 천차만별이다. 
나는 결국 리스트의 크기만큼 2번반복했다. 하지만 아래의 코드는 리스트의 크기를 21번 반복했지만 전화번호의 갯수가 21개가 넘어가는 순간부터 내가 압도적으로 불리하다. 또한 딕셔너리로 지정한 이유를 전혀 설명하지 못하였다.
"""