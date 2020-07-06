**题目链接**:
https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/

**解题思路**:
一开始我是这样子写的：

```python
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=len,reverse=True)
        s = list(s)
        s.sort()
        s = ''.join(s)
        sn = len(s)
        for i in d:
            d0 = i
            i = list(i)
            i.sort()
            i = ''.join(i)
            dn = len(i)
            s1,d1 = 0,0
            while s1<sn and d1<dn:
                if s[s1]!=i[d1]:s1+=1
                elif s[s1]==i[d1]:
                    s1+=1
                    d1+=1
            if d1==dn:return d0
        return ''

```
这个代码有两个问题：  
1.对列表那个排序，不应噶按照长度来排序，根据题目要求，应该是长度相等的情况下按照字典顺序排列(就是按照字母顺序排列)， 不过还是不理解这个d.sort(key = lambda x: [-len(x), x])是怎么做到的。  
2.对于两个对比的字符串，我对他们进行排序是因为理解错了，举个例子，abda和aab，这两个能匹配吗？我以为是能的，以为可以不按顺序，但是题目是删除后，就是说还是要按顺序啊，按顺序的话，这个就不能 匹配了。
对他们排序的话，就打乱了他们的顺序了，不合题目意思。
