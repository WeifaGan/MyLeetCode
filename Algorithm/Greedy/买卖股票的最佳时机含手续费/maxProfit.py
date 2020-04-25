class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy = in_hand = prices[0]
        ans = 0
        for price in prices[1:]:
            if in_hand > price :
                in_hand = price
            elif price - fee > in_hand:
                ans += price - fee - in_hand
                in_hand = price - fee
        return ans
