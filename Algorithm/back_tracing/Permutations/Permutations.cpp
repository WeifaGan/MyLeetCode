class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        int len=nums.size();
        vector<int> templist;
        vector<vector<int>> list;
        int start=0;
        backtrace(list,templist,nums,start,len);
        return list;
        
    }
    void backtrace(vector<vector<int>>& list,vector<int> templist,vector<int> nums,int start,int len)
    {
        if(templist.size()==len){list.push_back(templist);}
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
    }
};
