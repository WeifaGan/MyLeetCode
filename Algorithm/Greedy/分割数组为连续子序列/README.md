**题目链接**  
https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences/  

**题目描述**  

输入一个按升序排序的整数数组（可能包含重复数字），你需要将它们分割成几个子序列，其中每个子序列至少包含三个连续整数。返回你是否能做出这样的分割？

**示例 1：**
```
输入: [1,2,3,3,4,5]
输出: True
解释:
你可以分割出这样两个连续子序列 : 
1, 2, 3
3, 4, 5
```

**示例 2：**
```
输入: [1,2,3,3,4,4,5,5]
输出: True
解释:
你可以分割出这样两个连续子序列 : 
1, 2, 3, 4, 5
3, 4, 5
 ```

**示例 3：**
```
输入: [1,2,3,4,4,5]
输出: False
```

**解题思路**  
* 用哈希表nc[i]元素i在原始数组中的元素个数
* tail[i]记录在符合题意以i结尾的子序列,初始化为0
* 如果i,i+1,i+2，那么他们会组成子序列，nc[i]--,nc[i+1]--,nc[i+2]--,tail[i+2]++
* 后面如何有i+3，应该让i+3接上，那么nc[i+3]--.tail[i+2]--,tail[i+3]++
* 举个例子[1,2,3,3,4,5,6]
  * 初始化nc[1]=nc[2]=nc[4]=nc[5]=1,nc[3]=2,tail[i]=0
  * 第一个元素，检查nc[1], 因为有nc[1],nc[2],nc[3]不为0,所以让他们组成子序列，则nc[1]=nc[2]=0,nc[3]=1,tail[3]=1
  * 第二个元素，检查nc[2],为0，跳过
  * 第三个元素，检查nc[3]，为1，因为有nc[3],nc[4]和nc[5]不为0，所以他们组成子序列，nc[3]=nc[4]=nc[5]=0，tail[5]=1
  * 第四个元素，检查nc[3]，为0，跳过，第五个元素，第六个元素同理
  * 第七个元素，检查nc[6], 不为0，看能否接上前面的子序列，发现tail[5]=1,可以接上，所以nc[6]=0,tail[5]=0,tail[6]=1
 * 不满足以上条件
  * nc[i]后不能形成子序列和不能接上子序列，所以返回F
  * 循环完返回T
