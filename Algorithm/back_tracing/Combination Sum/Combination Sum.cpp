class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> templist;
        vector<vector<int>>list;
        int start=0;
        int remain=target;
        backtrace(list,templist,candidates,remain,start);
        return list;
        
    }
    void backtrace(vector<vector<int>> &list,vector<int>templist,vector<int>candidatates,int remain,int start)
    {
        if(remain<0) return;
        if(remain==0) list.push_back(templist);
        for(int i=start;i<candidatates.size();i++)
        {   
            
            templist.push_back(candidatates[i]);
            backtrace(list,templist,candidatates,remain-candidatates[i],i);
            templist.pop_back();
        }

    }    
};
