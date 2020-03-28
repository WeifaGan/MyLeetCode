class Solution {
struct cmp
{#正常定义是greater<int>，但是这进堆是一对的，所以如果对比大小呢,这就要定义greater函数了。
    bool operator()(pair<int,int>a,pair<int,int>b)
    {
        return a.first>b.first;
    }
};
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
       
    priority_queue<pair<int,int>,vector<pair<int,int>>,cmp>q;
    int M = matrix.size();
    int N = matrix[0].size();
    vector<vector<int>>used(M,vector<int>(N,0));
    q.push({matrix[0][0],0*N+0});
    int count=0;
    int result;
    while(count<k)
    {
        result = q.top().first;
        
        int m = q.top().second/N;
        int n = q.top().second-m*N;
        q.pop();
        if(m+1<M&&used[m+1][n]==0)
        {
            q.push({matrix[m+1][n],(m+1)*N+n});
            used[m+1][n]=1;
            
        }
        if(n+1<N&&used[m][n+1]==0)
        {
            q.push({matrix[m][n+1],m*N+(n+1)});
            used[m][n+1]=1;
        }
        
        count++;
    }
    return result;   
}
};
