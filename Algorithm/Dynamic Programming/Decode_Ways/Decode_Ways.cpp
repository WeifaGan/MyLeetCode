class Solution {
public:
	int numDecodings(string s) {
	const int len = s.length();
		if (s[0] == '0')return 0;
		int v[len + 1];
		v[1] = v[0] = 1;
		for (int i = 2; i<len+1; i++)
		{
			if (s[i-1] != '0')v[i] = v[i - 1];
			else
			{
				v[i] = 0;
			}
        int value=s[i-1]-'0';
			if (s[i - 2] == '1' || s[i - 2]=='2'&&value<=6)
			{
				v[i] += v[i - 2];
			}

		}
		return v[len];
    }   
};
