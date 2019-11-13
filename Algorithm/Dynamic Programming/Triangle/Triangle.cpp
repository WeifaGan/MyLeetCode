class Solution {
public:
    
     int minimumTotal(vector<vector<int>>& triangle) {
     int leng_1=triangle.size(); 
 
     int sum=0;
     int pos=0;
     for(int i=1;i<leng_1;i++)
     {
         for(int j=0;j<=i;j++)
         {
             if(j==0)
             {
                 triangle[i][j]=triangle[i-1][j]+triangle[i][j];
             }
             else if(j==i)
             {
                 triangle[i][j]=triangle[i-1][j-1]+triangle[i][j];
             }
             else   
             {
                  triangle[i][j]=min(triangle[i-1][j-1],triangle[i-1][j])+triangle[i][j];
             }     
         }
     }
     return *min_element(triangle[leng_1-1].begin(),triangle[leng_1-1].end());
    }
};
