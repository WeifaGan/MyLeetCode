class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        stack<int>mystack;
        map<int,int>mymap;
        int n2=nums2.size();        
        for(int i=n2-1;i>=0;i--)
        {
           
             while(!mystack.empty()&&mystack.top()<nums2[i])
            {
                mystack.pop();
            }
            if(mystack.empty()){mymap[nums2[i]]=-1;}
            else{mymap[nums2[i]]=mystack.top();}
            
            mystack.push(nums2[i]);               
        }
    
            int n1=nums1.size();
            vector<int>result(n1);
            for(int i=0;i<n1;i++)
            {
                result[i]=mymap[nums1[i]];
            }
         return result;
            
        }
};
