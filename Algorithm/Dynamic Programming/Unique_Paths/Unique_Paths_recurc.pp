class Solution {
public:
	int uniquePaths(int m, int n) {
		if (m == 0 || n == 0)return 0;
		vector<int>tag(m*n, 1);
		int x = m - 1;
		int y = n - 1;

		return traceback(x, y);
	}
	int traceback(int x, int y)
	{
		if (x == 0 || y == 0)return 1;
		if (x == 1 && y == 1)return 2;
		return traceback(x - 1, y) + traceback(x, y - 1);
	}
};
