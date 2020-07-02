**题目链接**:
https://leetcode-cn.com/problems/smallest-difference-lcci/


**解题思路**:
* 很明显这里用到双指针，但是具体如何操作，还是不太清晰，写了下面的程序：
```python
class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        if not a or not b:return 0
        a.sort()
        b.sort()
        n_min = abs(a[0]-b[0])
        for i in a:
            for j in b:
                n_min=min(abs(i-j),n_min)

                if j>i:break
        return n_min
```
发现超时了，与其说是这是双指针，还不如说两个迭代算了。**如果说是双指针，那你的指针呢？还有对指针的操作呢？**

* 如果发现b[i]>a[j],那么i指针应该加1，这样是往差值最小的方向走！
