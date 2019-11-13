class Solution {
public:
    void reverseString(vector<char>& s) {
        
        int size=s.size();
        for (int i=0,j=size-1;i<size/2,j>=size/2;i++,j--)
        {
            swap(s[i],s[j]);
        }
      
    }
            
    void swap(char &a,char &b)
        {
            char c=a;
            a=b;
            b=c;
        }
        
    
};
