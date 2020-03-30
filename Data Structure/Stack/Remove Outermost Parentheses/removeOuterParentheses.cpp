class Solution {
public:
    string removeOuterParentheses(string S) {
        int n = S.length();
        stack<char>mystack;
        
        string S1;
        for(int i=0;i<n;i++)
        {
            if(mystack.empty())
            {
                
                mystack.push(S[i]);
            }
            else if(mystack.top()==S[i])
            {               
                mystack.push(S[i]);
                S1+=S[i];
            }
            else
            {mystack.pop();
             if(!mystack.empty())
             {S1+=S[i];}
            }
        }
        return S1;
        
    }
};
