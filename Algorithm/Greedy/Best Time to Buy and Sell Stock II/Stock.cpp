class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int max=0;
        for(int i=0;i<prices.size();i++)
        {
            if(i+1<prices.size()&&prices[i+1]>prices[i])
                max=max+prices[i+1]-prices[i];
        }
        return max;
    }
};
