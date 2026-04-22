class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [] 

        for i in range(len(nums)):            
            if i > 0 and nums[i] == nums[i - 1]:
                continue   

            l, r = i + 1, len(nums) - 1      
            
            while l < r:
                summ = nums[i] + nums[l] + nums[r]

                if summ < 0:
                    l += 1

                elif summ > 0:
                    r -= 1
                
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    left, right = nums[l], nums[r]

                    while l < r and nums[l]  == left:
                        l += 1
                    while l < r and nums[r] == right:
                        r -= 1
        return res

        #Time: O(n^2)
        #Space: O(1)

                    
                    
               
            
            
                   
                    
                        
                
                    
                       




                #[-4,-1,-1,0,1,2]


        
        