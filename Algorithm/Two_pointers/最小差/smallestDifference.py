class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()
        na,nb = len(a), len(b)
        ia,ib = 0,0
        nmin = float('inf')
        while ia<na and ib<nb:
            if b[ib]>a[ia]:
                nmin = min(nmin,b[ib]-a[ia])
                ia+=1
            elif b[ib]<a[ia]:
                nmin = min(nmin,a[ia]-b[ib])
                ib+=1
            else: 
                return 0

        return nmin
