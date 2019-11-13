**题目链接**  
https://leetcode.com/problems/unique-binary-search-trees/  

**题目描述**   
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?  
**example**  
```
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

**解题思路**  
**总体思路**:动态规划  
* 设dp[n]为1..n的独立BTS数量
* sum=1为根的BTS数量+2为根的BTS的数量+3为根的BTS数量+...+n为根的BTS数量  
* 1为根时候,左子树结点数为0，右子树结点数为1，dp[n]=dp[0]*dp[n-1-0]  
* 2为根时候，左子树结点数为1，右子树结点数为2，dp[n]=dp[1]*dp[n-1-1] 
* i为根时候，左子树结点数为1，右子树结点数为2，dp[n]=dp[i]*dp[n-i-1] 
* 以此类推，dp[n]=dp[0]*dp[n-1-0]+dp[1]*dp[n-1-1]+...+dp[n-1]dp[0]  

**为什么可以用动态规划**    
一上来，其实想到的只有回溯了。这属于求组合吧，求组合也可以理解为求最优了，只是只有一个最优罢了。所以求组和可以往回溯和动态规划的方向想。

**如何寻找状态转移矩阵**  
通常来说求什么，dp状态就是代表什么，具体变量有哪些，就看题目有哪些变量了。
