**题目链接**:  
https://leetcode-cn.com/problems/max-consecutive-ones-iii/

**解题思路**：  
* 开始想的时候就想着左右指针里面0的个数就肯定是k了，这样子不对，应该是少于等于k。
* 看看下面的区别：
```python
 if right<lgth:

    if A[right]==0:
        K -= 1
    if K>=0:
        opmax = max(opmax,right-left+1)
    else:break
```
```python
if R < len(nums):
    summation += nums[R]
if summation >= s:
    optim = min(optim, R - L + 1)
    break
```
前者的最优值比较是在right<lgth,但是后者的最优值比较不在R<len()里面呢？细致看看，一个求最大值，一个求最小值，这就是区别啊。
