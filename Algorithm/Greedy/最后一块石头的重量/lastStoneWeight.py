from heapq import heapify, heappush, heappop
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapify(stones)
        while len(stones)>0:
            if len(stones) == 1: return -heappop(stones)
            y = heappop(stones)
            x = heappop(stones)
            if x != y: heappush(stones,y-x)
        return 0
