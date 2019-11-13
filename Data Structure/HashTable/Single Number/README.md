**题目链接** 
https://leetcode.com/problems/single-number/  

**题目描述**  
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
**Note:** Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
```
Input: [2,2,1]
Output: 1
```

**解题思路**  
  * 因为数组里面的元素都是除了只有一个，就是有两个了。所以用哈希表，进一个，检查到已经存在了就删了该元素，遍历所有元素后就只剩下那一个元素了。
  * 当哈希表只有一个数的时候，这个数是啥不知道，只能遍历原来数组看在map里面能不能找到了。
  
**疑惑**  
在leetcode上面编译不通过，在本地IDE就可以了。
