class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n=nums.size();
        stack<int>mystack;
        vector<int>result(n);
        int j;
        for(int i=n+n-1;i>=0;i--)
        {
            if(i>=n){j=i-n;}
            else{j=i;}
            while(!mystack.empty()&&nums[j]>=mystack.top())
            {
                mystack.pop();
            }
            if(j==i)
            {
            if(mystack.empty()){result[j]=-1;}
            else{result[j]=mystack.top();}
            }            
            mystack.push(nums[j]);            
        }
        return result;
        
    }
};
