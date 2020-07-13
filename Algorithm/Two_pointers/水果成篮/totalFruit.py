class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        left, right= 0,-1
        lgth = len(tree)
        opmax = 0
        st = list()
        zl  = 0 
        while right<lgth:
            while right<lgth:
                right+=1
                if right<lgth:
                    if tree[right] not in st:
                        zl +=1
                    st.append(tree[right])
                    if zl<=2:
                        opmax =max(opmax,right-left+1) 
                    else :break
            if right==lgth:break
            while left<right:
                del st[0]
                if tree[left] not in st:
                    zl -=1
                left+=1
                if zl<=2:
                    break
        return opmax
