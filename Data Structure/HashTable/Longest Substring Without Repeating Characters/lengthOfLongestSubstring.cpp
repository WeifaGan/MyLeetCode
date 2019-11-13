class Solution {
public:
	int lengthOfLongestSubstring(string s) {

		unordered_map<char, int>str_map;
		int left = -1;
		int res = 0;
		for (int i = 0; i < s.length(); i++)
		{
			if (str_map.find(s[i]) != str_map.end() && str_map[s[i]]>left)
			{
				left = str_map[s[i]];

			}
			res = res < i - left ? i - left : res;
			str_map[s[i]] = i;
		}

		return res;

	}
	
	int lengthOfLongestSubstring1(string s) {

		unordered_map<char, int>str_map;
		int left = -1;
		int res = 0;
		cout << str_map['k'];
		for (int i = 0; i < s.length(); i++)
		{
			if (str_map.find(s[i]) != str_map.end() && str_map[s[i]]>left)
			{
				cout<<(str_map[s[i]]);
				left = str_map[s[i]];

			}
			res = res < i - left ? i - left : res;
			str_map[s[i]] = i;
		}
		

		return res;

	}
};
