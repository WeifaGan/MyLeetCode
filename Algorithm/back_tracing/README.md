**回溯法**  
一种暴力试错法(列举)，往某个方向走，如果发现走不通，在往另外一个方向走。其核心思想是递归

**通用写法**  
以组合和为例https://leetcode.com/problems/combination-sum/  
function backtrace(list,templist,nums,remain,start)  
 {  
 //1.需要全局的list  
 if (remain<0) return;//2.要有出口  
 if(remain==0) list.push([templist])  
 for(let i=0;i<start;i++)  
 {  
    templist.pust(nums[i]);  
    backtrace(list,templist,nums,remain-nums[i],i);//3.递归的参数ing该是随着递归的次数改变而改变的  
    templist.pop();  
 }  
 }
 
