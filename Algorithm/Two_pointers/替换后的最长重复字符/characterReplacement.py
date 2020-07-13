class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right=0,-1
        lgth = len(s)
        opmax = 0
        d = defaultdict(int)
        fremax = 0
        while right<lgth:
            while right<lgth:
                right += 1
                if right<lgth:
                    d[s[right]] += 1
                    fremax = max(fremax,d[s[right]])
                    if right-left+1-fremax<=k:
                        opmax = max(opmax,right-left+1)
                    else:break
            if right==lgth:break
            while left<right:
                d[s[left]]-=1
                left+=1
                fremax_letter = max(d,key=d.get)
                if right-left+1-d[fremax_letter]<=k:
                    break
        return opmax
