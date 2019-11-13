**题目链接**  
https://leetcode.com/problems/remove-duplicates-from-sorted-array/  

**题目描述**  
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by **modifying the input array in-place** with O(1) extra memory.  
**example**  
```
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
```

**解题思路** 
* 用一个for循环，统计当前的数字与前一个相同，就跳过，否则加1。我以为这样子就可以了，其实没有满足题意，题目要求去除重复的数字并返回长度，如果没去除
重复的数字，尽管长度对了，输出的的数组也不对。
* 我们可以在原来的数组中修改，让前n个是对的。譬如说[1,1,2]修改成[1,2,2]并返回2，[0,0,1,1,2,2,3,3]修改成[0,1,2,3,2,2,3,3]并返回4。要完成这样子的修改
，即后面的要赋值给前面的，所以就需要两个指针了，一前一后。让i指向前，j指向后。因为i,j位置不同，所以当nums[i]=nums[j]的时候，说明有数字重复。因为我们要给
j这个位置赋值一个不重复的值，所以这时候j继续往后走，当nums[i]!=nums[j]时候，i+1,是为了让i走到j之前的位置，就可以nums[j]赋值给nums[i]了。

**MySubmission**  
* runtime beats 30.28%  
* memory beats 87.5%  
