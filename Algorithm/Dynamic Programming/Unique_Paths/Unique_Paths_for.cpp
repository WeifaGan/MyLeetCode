class Solution {
public:
	int uniquePaths(int m, int n) {
		if (m == 0 || n == 0)return 0;
		const int x = m;
		const int y = n;
		vector<int>tag(m*n,1);
		return count(m, n, tag);
	}
	int count(int x, int y, vector<int>&tag)
	{
		for (int i = 1; i<y; i++)
		{
			for (int j = 1; j<x; j++)
			{
				tag[i*x + j ] = tag[i*x + j-1] + tag[(i - 1)*x + j];
			}
		}
		return tag[x*y-1];
	}

};
