class Solution {
public:
	vector<vector<string>> partition(string s) {
		vector<string>templist;
		vector<vector<string>>list;
		string splitStr;
		int start = 0;
		backtrace(s, list, templist, splitStr, start);
		return list;
	}
	void backtrace(string s, vector<vector<string>>&list, vector<string>templist, string splitStr, int start)
	{
		bool flag = true;
		if (start >= s.length()) { list.push_back(templist); return; }
		for (int i = 1; start+i<=s.length(); i++)//控制间隔
		{
			splitStr = s.substr(start, i);
			if (!isPalindrome(splitStr,true)) { continue; }
		    else{ templist.push_back(splitStr); }
			backtrace(s, list, templist, splitStr, start+i);
			templist.pop_back();
		}
	}
	bool isPalindrome(string s,bool flag) {
		for (int start = 0,end=s.length()-1; start< s.length() / 2;start++,end--)
		{
			flag = flag&&s[start] == s[end];
		}
		return flag;
	}
 };
