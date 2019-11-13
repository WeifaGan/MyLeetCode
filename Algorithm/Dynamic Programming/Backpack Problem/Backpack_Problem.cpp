class solution {
public:
	int backpack(vector<int> w, vector<int> v, int C)
	{
		int n = w.size();
		if (C == 0||n==0)return 0;
	
		vector<vector<int>>dp(n, vector<int>(C+1));
		for (int i = 0; i < n; i++)
		{
			dp[i][0] = 0;
		}
		for (int i = 0; i <=C; i++)
		{
			dp[0][i] = i>=w[0]?v[0]:0;
		}

		for (int i = 1; i < n; i++)
		{
			for (int j = 1; j <=C; j++)
			{
				if (j - w[i - 1]>=0)
				{dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i- 1]); }
			}
		}
		
		return dp[n - 1][C];
	}
//为什么是C+1,而不是C，应d[i][j]的j表示容量，如果长度为C，最多也就C-1-w[i]，但是我们需要C-w[i]。
//时间复杂度分析：时间O(n*C),空间O(n*C)。以下用一维数组来记录数据。
//但要注意的是我们需要从后往前计算，不然dp[j - w[i - 1]]可能是已经被更新了的数据，

	int backpack1(vector<int> w, vector<int> v, int C)
	{
		int n = w.size();
		if (C == 0 || n == 0)return 0;

		vector<int>dp(C + 1);
	
		for (int i = 0; i <= C; i++)
		{
			dp[i] = (i>= w[0] ? v[0] : 0);
		}

		for (int i = 1; i < n; i++)
		{
			for (int j = C; j >= 0; j--)
			{
				if (j - w[i - 1] >= 0)
				{
					dp[j] = max(dp[j], dp[j - w[i - 1]] + v[i - 1]);
				}
			}
		}

		return dp[C];
	}
	
};
