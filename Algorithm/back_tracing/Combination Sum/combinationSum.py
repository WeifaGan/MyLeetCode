class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        lst = []
        n = len(candidates)
        def backtrace(i,tep,remain):
            if remain < 0: return
            elif  remain == 0:
                lst.append(tep)
                return 
            for j in range(i,n):
                if remain - candidates[j]<0:break
                backtrace(j,tep+[candidates[j]],remain-candidates[j])
        backtrace(0,[],target)
        return lst
