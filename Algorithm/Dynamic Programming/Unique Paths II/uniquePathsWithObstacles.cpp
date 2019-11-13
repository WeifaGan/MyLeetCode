class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        
        int sizex=obstacleGrid[0].size();
        int sizey=obstacleGrid.size();
        // vector<vector<long>>dp(sizey,vector<long>(sizex));
        // dp[0][0]=1;
        vector<long>dp(sizex);
        dp[0]=1;
        for(int i=0;i<sizey;i++)
        {
            for(int j=0;j<sizex;j++)
            {
                if(obstacleGrid[i][j]==0)
                {
                   
                    if(i-1>=0&&j-1>=0)
                    {
                         dp[j]= dp[j]+ dp[j-1];
                    }
                    else if(i-1>=0&&j-1<0)
                    {
                         dp[j]= dp[j];
                    }
                    else if(i-1<0&&j-1>=0)
                    {
                         dp[j]= dp[j-1];
                    }
                }
                else
                {
                     dp[j]=0;
                }
            
             }
        
        }
        return dp[sizex-1];
}
};
