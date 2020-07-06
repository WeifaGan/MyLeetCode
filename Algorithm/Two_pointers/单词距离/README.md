**题目连接**：
https://leetcode-cn.com/problems/find-closest-lcci/

**解题思路**：
双指针，不断更新两个word的距离，找最小的即可。

没想到怎么做，稍微看了一下别人的思路，写了这样子的代码：
```python
        n = len(words)
        left,right = 0, n-1
        find_word = [word1,word2]
        min_p = 0
        while left<right:
            if words[left] not in find_word:
                left += 1
            elif words[right] not in find_word or words[right]==words[left] :
                right -= 1
            else:
                min_p = right-left
                break

        while left<right:
            left+=1
            if 
```
这个代码是打算先找到两个单词的距离，然后再继续精细定位，因为break之后那是不一定是最小的，但是做不下了。我为什么对指针进行加减操作呢，主要是觉得双指针嘛，就是要对它加减操作啊。其实也不一定啊。
双指针有两个指针就行了，后面怎么弄看情况呀！  
好了，再仔细地看了一下别人地解法，再写了这个代码：
```python
class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int: 
        index1, index2 = 0, len(words)-1
        min_p = float('inf')
        for index, word in enumerate(words):
            if word == word1:
                index1 = index
            elif word == word2:
                index2 = index
            min_p = min(min_p,abs(index1-index2))
        return min_p
```
结果还是不对，原因在于一开始就定义了index1和index2，这样子对min地计算是有影响地。index1=0,如果一开始word2的index=1,那么min_p就只能是1了，不对！
