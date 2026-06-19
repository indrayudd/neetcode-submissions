class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums)//2

        lookup = {}

        def dp(curr, index):
            if (curr, index) in lookup:
                return lookup[(curr, index)]
            
            if curr == target:
                return True
            
            if curr> target or index >= n:
                return False

            res = dp(curr+nums[index], index+1)
            if not res:
                res = dp(curr, index+1)
            
            lookup[(curr, index)] = res
            return res
        return dp(0,0)

            


