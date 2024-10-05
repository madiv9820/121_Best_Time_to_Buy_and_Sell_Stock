# 121. Best Time to Buy and Sell Stock

__Type:__ Easy <br>
__Topics:__ Array, Dynamic Programming <br>
__Companies:__ Google, Amazon, Bloomberg, Microsoft, Meta, Zoho, TikTok, Apple, Uber, Infosys, tcs, Walmart Labs, Accenture, Zoox, IBM, Oracle, Morgan Stanley, Citadel, Samsung, Visa, Adobe, Goldman Sachs, Yahoo, Yandex, J.P. Morgan, Bolt, Nvidia, Media.net, PayPal, Tesla <br>
__Leetcode Links:__ [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)
<hr>

### Question

You are given an array `prices` where `prices[i]` is the price of a given stock on the <code>i<sup>th</sup></code> day.

You want to maximize your profit by choosing a __single day__ to buy one stock and choosing a __different day in the future__ to sell that stock.

Return _the maximum profit you can achieve from this transaction_. If you cannot achieve any profit, return `0`.
<hr>

### Examples

__Example 1:__

__Input:__ prices = [7,1,5,3,6,4] <br>
__Output:__ 5 <br>
__Explanation:__ Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5. <br>
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

__Example 2:__

__Input:__ prices = [7,6,4,3,1] <br>
__Output:__ 0 <br>
__Explanation:__ In this case, no transactions are done and the max profit = 0.
<hr>

### Constraints:

- <code>1 <= prices.length <= 10<sup>5</sup></code>
- <code>0 <= prices[i] <= 10<sup>4</sup></code>