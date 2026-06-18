class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        lookup = {} # str -> bool
        n = len(s)
        wordSet = set(wordDict)
        maxlen = max(len(word) for word in wordDict)

        def dp(st):

            # print("dp - ",st)

            if st in lookup:
                return lookup[st]

            if not st:
                return True



            for i in range(min(maxlen, len(st))):
                if st[0:i+1] in wordSet:
                    if dp(st[i+1:]):
                        lookup[st] = True
                        return True
            
            lookup[st] = False
            return False

        
        return dp(s)

        