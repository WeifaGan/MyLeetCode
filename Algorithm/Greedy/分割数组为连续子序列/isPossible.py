class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nc,tail = dict(),dict()
        for num in nums:
            if num not in nc:
                nc[num] = 1
            else:
                nc[num] = nc[num]+1
            tail[num] = 0

        for num in nums:
            if not nc[num]:continue
            elif nc[num] and  num-1 in tail and tail[num-1]:
                nc[num] = nc[num]-1
                tail[num-1] = tail[num-1]-1
                tail[num] = tail[num] + 1
            elif num+1 in nc  and  num+2 in nc and nc[num] and nc[num+1] and nc[num+2]:
                    nc[num] = nc[num] - 1
                    nc[num+1] = nc[num+1] - 1
                    nc[num+2] = nc[num+2] -1 
                    tail[num+2] = tail[num+2] + 1  
       # 两个elif不能颠倒，尽量前面的序列，贪心
            else:return False

        return True
