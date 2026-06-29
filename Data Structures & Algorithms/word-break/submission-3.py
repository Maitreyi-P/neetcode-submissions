class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        #checking for every word in dict

        dp = {}
        
        def rec(i):
            if i == len(s):
                dp[i] = True
                return True

            if i in dp:
                return dp[i]
            
            for w in wordDict:
                if i+ len(w) <= len(s) and s[i:i+len(w)] == w:
                    
                    if rec(i+len(w)):
                        dp[i] = True
                        return dp[i]

            dp[i] = False
            return dp[i]

        return rec(0)