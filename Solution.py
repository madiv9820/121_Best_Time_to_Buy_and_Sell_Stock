from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize max_Profit to 0 and set minimum_Stock_Price to the price on the first day
        max_Profit, minimum_Stock_Price = 0, prices[0]

        # Loop through the stock prices starting from the second day
        for current_Day in range(1, len(prices)):
            # Get the stock price on the current day
            current_Stock_Price = prices[current_Day]
            
            # Calculate profit if we were to sell on current_Day after buying at minimum_Stock_Price
            current_Profit = current_Stock_Price - minimum_Stock_Price
            
            # Update max_Profit if the current profit is greater than the previously recorded max_Profit
            max_Profit = max(max_Profit, current_Profit)
            
            # Update minimum_Stock_Price to the lowest price encountered so far
            minimum_Stock_Price = min(minimum_Stock_Price, current_Stock_Price)
        
        # Return the maximum profit found
        return max_Profit

# Time Complexity: O(n)
# The loop runs once through the list of prices, making the time complexity linear.

# Space Complexity: O(1)
# The space used is constant, as it only relies on a fixed number of variables regardless of the input size.