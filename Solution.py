from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize max_Profit to 0, which will hold the maximum profit found
        max_Profit, n = 0, len(prices)
        
        # Loop through each day except the last day
        for current_Day in range(n - 1):
            # Get the stock price on the current day
            current_Stock_Price = prices[current_Day]
            
            # Loop through the subsequent days to find future prices
            for next_Day in range(current_Day + 1, n):
                # Get the stock price on the next day
                future_Stock_Price = prices[next_Day]
                
                # Calculate the profit if bought on current_Day and sold on next_Day
                current_Profit = future_Stock_Price - current_Stock_Price
                
                # Update max_Profit if the current profit is greater than the previously recorded max_Profit
                max_Profit = max(max_Profit, current_Profit)
        
        # Return the maximum profit found
        return max_Profit

# Time Complexity: O(n^2)
# The outer loop runs n-1 times and the inner loop runs up to n times in the worst case,
# leading to a quadratic time complexity.

# Space Complexity: O(1)
# The space used does not depend on the size of the input list; we are using a constant amount of space.