**题目链接**  
https://leetcode.com/problems/subsets-ii/  

**题目描述**
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

**example**
```
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```

**解题思路**  
* 最主要还是避开重复的子集,一开始我是想着，向前+1判断是否有重复的数字，但是这样子容易出现出界带来一些问题，
有一个重要的地方忘记了，就是先排序，这样子就可以避免重复向后判断是否有重复的数字了。  
* 其实最重要是如何避免重复问题。一开始只是觉得避开重复的的条件是 j>0 and nums[j]==nums[j-1],但是后来发现这样子是不对的，譬如对于[1,2,2,2],
你无法选择[1,2,2]，最多选择[1,2]放进lst里面，但是[1,2,2]甚至[1,2,2,2]都是对的。其实我们应该做的是避免同一个层次的for循环中取重复的数，例如，
我们是选择了第一个2，就不会选择第二个2,因为这样子后续处理会出现重复。如果某个层次for循环从第一个2开始，该层次的下一个for循环从第二个2开始，那么这样两个for循环的第一个2是不用比对的，所以条件应该是j>i and nums[j]==nums[j-1]。

**My Submission**  
Your runtime beats 93.08 % of cpp submissions.  
Your memory usage beats 39.89 % of cpp submissions.
