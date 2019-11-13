class Solution {
public:
    int numTrees(int n) {
        
        int dp[n+1];
        dp[0]=1;
        int sum=0;
        for(int i=1;i<=n;i++)
        {
            sum=0;
            for(int j=0;j<=i-1;j++)
            {    
                sum=sum+dp[j]*dp[i-1-j];
            }
            dp[i]=sum;
        }
        return dp[n];
    
    }
};
