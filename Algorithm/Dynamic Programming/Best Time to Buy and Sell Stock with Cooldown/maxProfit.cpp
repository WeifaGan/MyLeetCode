class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int size=prices.size();
        if(size==0)return 0;
        vector<int>buy(size,0);     
        vector<int>sell(size,0); 
        vector<int>cooldown(size,0);
        buy[0]=-prices[0];
        for(int i=1;i<size;i++)
        {     
            cooldown[i]=max(sell[i-1],cooldown[i-1]);
            cooldown[i]=max(cooldown[i],buy[i-1]);
            sell[i]=max(buy[i-1]+prices[i],sell[i-1]);
            buy[i]=max(cooldown[i-1]-prices[i],buy[i-1]);     
        }
        int max_prf=max(buy[size-1],sell[size-1]);
        max_prf=max(max_prf,cooldown[size-1]);
        return max_prf;
        
    }
};
