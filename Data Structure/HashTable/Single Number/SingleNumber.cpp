class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int sz=nums.size();
        if(sz==0)return 0;
        map<int,int> int_map;
        for(int i=0;i<sz;i++)
        {
            if(int_map.find(nums[i])!=int_map.end())
            {
                int_map.erase(nums[i]);
            }
            else{int_map[nums[i]]=i;}
            
        }
        
        for(int i=0;i<sz;i++)
        {
            if(int_map.find(nums[i])!=int_map.end())
               {
                   return nums[i];
               }
        }
        
    }
};
