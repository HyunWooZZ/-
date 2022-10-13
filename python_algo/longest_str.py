class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque
        string_set = set()
        queue = deque()
        result = 0
        ###
        # 문자열을 deque와 set에 추가 > 겹치는게 생김 aswer 에 deque 길이 answer에 저장 > 해당 원소 나올때까지
        # deque leftpop 및 set에서 제거 > 반복
        ###
        
        for i in s:
            if i in string_set:
                result = max(result, len(list(string_set)))
                
                while True:
                    prev = queue.popleft()
                    string_set.remove(prev)
                    if prev == i:
                        break
                        
            queue.append(i)
            string_set.add(i)
        
        else:
            result = max(result, len(list(string_set)))    
        
        return result
                        