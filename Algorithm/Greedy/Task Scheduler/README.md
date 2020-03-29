**题目链接**  
https://leetcode.com/problems/task-scheduler/  

**题目描述**  
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

**example**  
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
```

**题目思路**
* 1.求最值，一般贪心算法或者动态规划，显然这里可以贪心算法
* 2.从例子中总结规律的(ABi)(ABi)AB,A的频率为3,然后就有2个(),间隔为2，每个()就有2+1个数字，AB的频率都为3,然后最后就多出2个字母AB了，这是频率为3的个数，
所以有(k-1)*(n+1)+p,其中k为top的频率，n为间隔,p为有着top频率的个数。
* 3.有特殊情况，就是不用插入idle的，这时候ans=tasks.size()了，所以到最后我们要比较一下2和3计算的结果，取最大值。
