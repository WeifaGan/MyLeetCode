class Solution {
public:
	string longestPalindrome(string s) {
		int len = s.length();
		if (len == 1) return s;
		vector<vector<int>>dp(len, vector<int>(len));
		string s1;
		int max = 0;
		for (int i = len-1; i>=0; i--)
		{
			for (int j = i; j<len; j++)
			{
				if (j-i==1||j-i==0)dp[i][j] = s[i] == s[j];
				else if(i+1<=len)dp[i][j] = dp[i + 1][j - 1] && s[i] == s[j];
				if (dp[i][j] && j - i >= max)
				{ 
					max = j - i;
					s1 = s.substr(i, j - i + 1); 
				}
			}
		}
		return s1;
	}
  }
