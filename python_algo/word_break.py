### 139. Word Break
### kadene 만 생각하지 말고, bottom up 도 생각하면서 다이나믹 프로그래밍을 고민해보자.
### greedy 생각은 좋았으나 엣지케이스 고려가 전혀 되지 않았음.
### 엣지 케이스에 대해 계속 고민하자.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(len(s)+1):
            if dp[i]: # 해당 단어부터 가능하다면..?
                for j in range(i+1, len(s)+1):
                    if s[i:j] in wordDict: ## 해당 단어까지 어떻게든 만들어지는 경우
                        dp[j] = True
        
        return dp[-1]