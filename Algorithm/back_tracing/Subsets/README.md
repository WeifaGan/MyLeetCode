**题目链接**  
https://leetcode.com/problems/subsets/  

**题目描述**  
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.  
**eample**  
```
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```
**解题思路**  
* 回溯法,一开始我也知道使用回溯法，但是就是不知道如何改变每个vector的长度，看来还是对回溯法不够熟悉
* 其实回溯法对于每个元素是尝试放进去和不放进去子集两种选择。首先把1放进子集，处理[2,3]，不放进1，放进2，处理[3]，不放进1，2，放进3,处理，没得处理了。所以第一层的循环是选择谁作为第一个元素放进子集，处理后续的事情，第二层循环是有了一个元素的基础上，再选择一个元素放进去子集(for循环i+1的原因)，处理后续的事情...(temlst+[num[j]]),所以for循环里面变量是元素选择和子集的选择。

**My Submisson**  
Your runtime beats 85.85 % of cpp submissions  
Your memory usage beats 29.63 % of cpp submissions
