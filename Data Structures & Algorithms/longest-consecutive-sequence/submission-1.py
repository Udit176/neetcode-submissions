class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

    
        curr_max = 1
        ans = 1
        nums = sorted(set(nums))

        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                curr_max += 1                
            else:
                curr_max = 1
            
            ans = max(curr_max, ans)
        
        return ans

        
        
        