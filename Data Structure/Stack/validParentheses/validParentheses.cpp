class Solution {
public:
	bool isValid(string s) {

		//除了false,其他就是true，所以找到false就行

		int len = s.length();
		if (len == 0)return true;
		if (len % 2 != 0)return false;
        vector<char>vec;
        for(int i=0;i<len;i++)
        {
            if(s[i]=='('||s[i]=='{'||s[i]=='[')
            {vec.push_back(s[i]);}
            else
               {
                    if(vec.empty())return false;
                    char c=vec.back();
                    if(s[i]==']'&&c!='[')return false;
                    if(s[i]=='}'&&c!='{')return false;
                    if(s[i]==')'&&c!='(')return false;
                    vec.pop_back();
               }
        }
        if(vec.empty())return true;
        else return false;
        }
};
