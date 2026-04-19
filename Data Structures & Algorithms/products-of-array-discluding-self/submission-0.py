class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod_left = 1
        prod_right = 1
        n = len(nums)

        answer = [1] * n

        for i in range(n):
            answer[i] = prod_left
            prod_left *= nums[i]

        for i in range(n - 1, -1, -1):
            answer[i] *= prod_right
            prod_right *= nums[i]

        return answer

        # Time: O(n)
        # Space: O(1)



           
        

        
            

            
            
                
       
            

            


            
        
