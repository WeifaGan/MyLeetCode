
**题目链接：**  
https://leetcode.com/problems/sort-colors/description/

**题目描述：**  
```
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.
```
**exmaple**
```
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```
**follow up**
* A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
* Could you come up with a one-pass algorithm using only constant space?

**解题思路：**    
* 该题本质上是排序问题，可以直接用冒泡等排序算法来做.  
* 自己的思路：用指针指向vector的一头一尾,对比大小后,把2往后放,把0往前放，把1往中间放,思路虽然比较简单,但是有很多需要注意的细节.  
  * 如果0在左,2在右,直接交换即可.  
  * 如果0在左,1在右,在0和1之间的位置，寻找一个2与1交换,使1往中间走.  
  * 如果1在左,2在右,在1和2之间的位置,寻找一个0与1交换,1往中间走,0往左走.  
  * 如果前后都为1,在中间找到0或者2，0与左边的1交换或者2与右面的1交换.  
  * 如果前后两个0,左边直接跳过.  
  * 如果前后两个0,右边直接跳过.  
* 还是推荐用第一种方法吧,简单又简洁

**My submission:**    
Your runtime beats 91.35 % of cpp submissions.  
Your memory usage beats 14.93 % of cpp submissions
