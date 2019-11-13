**题目链接**  
https://leetcode.com/problems/permutations-ii/  

**题目描述**  
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
**example** 
```
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```

*解题思路**  
* 通过位置的状态来判断该位置是否已经被push进去  
* 如何避免重复的templist被push进去list，是个难点。当第一个push进入的templist是[1,1,2,2],如果没有continue这个条件的判断,下一次push的是[1,1,2,2]，
但是数值对应的pos是不一样的，如下图所示。那么如何避免第二个同样的templist push进入呢？其实如果第三个位置的2被push进去templist了，那么第四个2肯定也会进去，
因为只有第四个位置的状态是false的。所以关键的在于防止第三个2被push进templsit,怎么做呢？其实程序是先访问第四个2再访问第三个2，所以当访问第四个2的时候，
第3个位置的2肯定是false，所以我们可以判断前一个2的位置状态，如果前一个2的位置状态是2的false时候，我们是不应该把这个2push进入templist里面了。  
![image](https://github.com/WeifaGan/MyLeetCode/blob/master/back_tracing/Images/1.PNG)
* 为什么不能像combinesum2那么判断呢 https://leetcode.com/problems/combination-sum-ii/  
原因是combinesum2里面backtrace是从i+1开的，而这里是从0开始的，当nums[i]=nums[i-1]时候，至少要两次的循环，那时候p>=2，所以p>1就不起作用了，条件被弱化了，排除了很多的可能性。
 ```
 for(int i=0;i<nums.size();i++)
  {  

      if(visited[i]) continue;
      p++;
      if(i>0&&p>1&&nums[i]==nums[i-1]){continue;}
      visited[i]=true;
      templist.push_back(nums[i]);
      backtrace(list,templist,nums,visited);
      templist.pop_back();
      visited[i]=false;
  }
 ```

