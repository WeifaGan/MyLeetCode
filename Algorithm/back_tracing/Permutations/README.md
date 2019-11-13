**题目链接**  
https://leetcode.com/problems/permutations/  

**题目描述**  
Given a collection of distinct integers, return all possible permutations.
```
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

**解题思路**  
* 主要是判断vecotr里面是否已经包含当前指向的值了，如果有了，就跳过，这个判断用的是for循环，还有其他好有一点方法吗？
* 对前一点更新一下。相比于用for循环来判断，参考了一个更好的方法：对于已经用力的数字，我们给它的位置做个标记就行了，下一个回溯，就看对应的位置的标记就行了。
改前：
```
 for(int i=start;i<len;i++)
        {
            int flag=false;
            for(int j=0;j<templist.size();j++)
            {
                if(nums[i]==templist[j])
                {flag=true;
                break;     }           
            }
            if(flag){continue;} 
            templist.push_back(nums[i]);
            backtrace(list,templist,nums,start,len);
            templist.pop_back();
            
        }
```
改后：
```
  for(int i=0;i<nums.size();i++)
        {   
            
            if(visited[i]){ continue;} 
            visited[i]=true;
            templist.push_back(nums[i]);
            backtrace(list,templist,nums,visited);
            templist.pop_back();
            visited[i]=false;          
        }
```
但是不知道为啥，改后速度更慢一些。
