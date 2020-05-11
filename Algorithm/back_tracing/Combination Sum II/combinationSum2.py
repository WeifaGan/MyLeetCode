class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        n  = len(candidates)
        lst = []
        def backtrace(i,temp,remain):
            if remain == 0:
                lst.append(temp)
                return
            for j in range(i,n):
                if j>i and candidates[j]==candidates[j-1]:continue
                if remain-candidates[j]<0:break
                backtrace(j+1,temp+[candidates[j]],remain-candidates[j])
        
        backtrace(0,[],target)
        return lst
