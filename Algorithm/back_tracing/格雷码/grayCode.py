class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n ==0: return [0]
        if n == 1: return [0,1]
        res = []
        def backtrace(k,path,res):
            if k==n:return res.append(path[:])
            temp = [ ]
            for i in range(0, len(path), 2):
                temp.append(path[i]*2+0)
                temp.append(path[i]*2+1)
                temp.append(path[i+1]*2+1)
                temp.append(path[i+1]*2+0)
            backtrace(k+1,temp[:],res)

        path=[0,1]
        backtrace(1,path,res)
        return res.pop()
