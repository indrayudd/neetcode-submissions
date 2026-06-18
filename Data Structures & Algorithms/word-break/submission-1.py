class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        lookup = {} # str -> bool
        n = len(s)
        wordSet = set(wordDict)

        def dp(st):

            # print("dp - ",st)

            if st in lookup:
                return lookup[st]

            if not st:
                return True



            for word in wordSet:
                # print("word - ", word)
                for i in range(len(st)):
                    # print("comparing", word, "to", st[:i+1])
                    if st[:i+1] == word:
                        # print("pass, calling dp(", st[i+1:],")")
                        if dp(st[i+1:]):
                            lookup[st] = True
                            return True
            
            lookup[st] = False
            return False

        
        return dp(s)

        