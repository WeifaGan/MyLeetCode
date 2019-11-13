class Solution {
public:
    int maxArea(vector<int>& height) {
        
        int size=height.size();
        if(size==0) return 0;
        int left=0;
        int right=size-1;
        for(int i=0,j=size-1;i<j;)
        {
            if(height[i]<height[j])
            {
                i++;
            }
            else{j--;}
            if(i-1>=0&&height[i-1]<height[i]||j+1<size&&height[j]>height[j+1])
            {
               
                int cur_area=(j-i)*(height[i]>height[j]?height[j]:height[i]);
                int bf_max=(right-left)*(height[left]>height[right]?height[right]:height[left]);
                if(bf_max<cur_area)
                {
                    left=i;
                    right=j;                    
                }
            }
        }   
        return (right-left)*(height[left]>height[right]?height[right]:height[left]);
    }
};
