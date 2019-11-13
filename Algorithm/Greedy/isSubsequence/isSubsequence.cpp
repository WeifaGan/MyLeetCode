class Solution {
public:
    bool isSubsequence(string s, string t) {
        int sindex=0;
        for(int i=0;i<t.size();i++)
        {
            if(s[sindex]==t[i])
            {sindex++;}
        }
        return sindex==s.size();
    }
};
