class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int leng_y=grid.size();
        int leng_x=grid[0].size();
     
        for(int i=0;i<leng_y;i++)
        {
            for(int j=0;j<leng_x;j++)
            {
                if(i==0&&j==0)
                {grid[i][j]=grid[i][j];}
                else if(i==0)
                {grid[i][j]=grid[i][j-1]+grid[i][j];}
                else if(j==0)
                {grid[i][j]=grid[i-1][j]+grid[i][j];}
                else
                {grid[i][j]=min(grid[i-1][j],grid[i][j-1])+grid[i][j];}
            }
        }
        return grid[leng_y-1][leng_x-1];   
    }
};
