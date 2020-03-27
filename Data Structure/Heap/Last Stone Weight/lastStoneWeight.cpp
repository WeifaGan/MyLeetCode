class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int>mystones;
        int n=stones.size();
        for(int i=0;i<n;i++)
        {
            mystones.push(stones[i]);
        }
        
        while(mystones.size()>1)
        {
            int top1 = mystones.top();
            mystones.pop();
            int top2 = mystones.top();
            mystones.pop();
            if(top1!=top2)
            {
                mystones.push(top1-top2);
            }
           
        }
        if(mystones.empty())
        {
            return 0;
        }
        else{return mystones.top();}
    }
};
