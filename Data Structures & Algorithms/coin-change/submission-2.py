class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort(reverse=True)
        # coinSet = set(coins)
        lookup = {}

        def dp(amt):

            if amt in lookup:
                return lookup[amt]
            
            if amt == 0:
                return 0
            
            # if amt < 0:
            #     return count - 1

            new_count = float('inf')

            for coin in coins:
                
                if amt - coin >= 0:
                    verdict = dp(amt-coin)
                    if verdict != -1:
                        new_count = min(new_count, verdict+1)
                

            if new_count == float('inf'):
                lookup[amt] = -1
                return -1
            
            lookup[amt] = new_count
            return new_count
        
        return dp(amount)

        