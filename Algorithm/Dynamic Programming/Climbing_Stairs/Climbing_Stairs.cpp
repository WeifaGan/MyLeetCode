class Solution {
public:
    int climbStairs(int n) {
        if(n<=0)return 0;
        if(n==1)return 1;
        const int len=n+1;
        int v[len];
        v[0]=v[1]=1;
        for(int i=2;i<n+1;i++)
        {
            v[i]=v[i-1]+v[i-2];
        }
        return v[n];
    
    }
};
