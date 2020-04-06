**题目链接**  
https://leetcode.com/problems/next-greater-element-i/

**题目描述**  
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

**example**  
```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
    
```

**解题思路**  
* 自己想不到用栈的方法怎么做
* 思路是nums2从后面开始进栈，第一，进栈时候如果是空的，即为-1。第二，top元素比即将进栈的小，就pop出来，直到有比即将进栈的大，那么即将进栈的元素的下一个
更大的就是top元素了。
