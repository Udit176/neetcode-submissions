class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price, max_profit = prices[0], 0

        for price in prices:

            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit          
        
        return max_profit

        #Time: O(n)
        #Space: O(1)

            

         
           




        