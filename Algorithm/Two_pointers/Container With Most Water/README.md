**题目链接**  
https://leetcode.com/problems/container-with-most-water/  

**题目描述**  
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn 
such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such 
that the container contains the most water.  
**Note:** You may not slant the container and n is at least 2.

**解题思路**  
* 暴力法？太暴力了，不行
* Two Pointers,因为有前后有两条竖线，所以很自然就想到用Two Pointers的方法了。
  * 主要思路是如果当前的面积比之前最大的面积还大，我们就更新最大面积，但是难点在于在某一次的循环中如何确定左指针还是右指针移动。
  * 移动左指针还是右指针？因为左右指针都是往里面靠拢的，所以宽度一直在减少，但是如果遇到更高的竖线，就可以抵消宽度带来面积的减少。因为高度只是取决于左右
  两指针指向的最短的竖线，所以我们只需要移动短竖线对应的指针即可。
  * 那么如果移动的是高竖线对应的指针，结果会怎么样呢？第一，移动了该指针，指向了更高的竖线，那么对应的面积肯定是减少的。因为高度没变，宽度减少了。
  第二，移动该指针，指向更短的竖线，那么面积肯定也减少了，因为高度和宽度都减少了。所以要得到更大的面积，就要移动短竖线对应的指针，这才有可能得到更大的
  面积。
  * 如果两条竖线都一样，移动哪个指针？第一，如果目前的面积已经是最大了，那么不管你移动哪个指着，都没关系，因为最大的已经确定下来了，后面的怎么移动已经没
  影响了。第二，如果目前的面积不是最大，但是之后最大的面积的短边是目前两边中的一条，那么也没关系，因为目前指针对应的竖线高度一样，不管你用左边的竖线还是右边
  的竖线，面积都一样。第三，如果目前的面积不是最大，但是之后最大的面积的短边都不是目前两边中其中一边。这种情况说明目前两边的中间某些地方有两条很高的边弥补了
  宽度的减少。其实不管你先移动那个指针，最后两个指针都要指向另外最高的那两条边，因为我们总是移动对应的短边的指针。
  
 **My submission**  
 * run time beats 66.30%
 * Memory Usage beats 67.01%
