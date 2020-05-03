class Solution(object): 
    def isPossibleDivide(self, nums, k): 
        """ :type nums: List[int] :type k: int :rtype: bool """ 
        mymap = collections.defaultdict(int) 
        for i in nums: mymap[i] += 1 
        lst = sorted(nums)
        for i in lst:
            while mymap[i]:
                for c in range(k):
                    if mymap[i+c] == 0: return False
                    mymap[i+c] -= 1             
        return True
