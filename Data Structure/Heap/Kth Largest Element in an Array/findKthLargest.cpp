class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int,vector<int>,greater<int>> klarge;
        int n = nums.size();
        for(int i=0;i<n;i++)
        {
            if(i<k)
            {
                klarge.push(nums[i]);
            }
            else
            {
                if(nums[i]>klarge.top())
                {
                    klarge.pop();
                    klarge.push(nums[i]);
                }
            }
        }
        return klarge.top();
    }
};
