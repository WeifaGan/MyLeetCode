class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int>smulate_stack;
        queue<int>my_queue;
        int n=pushed.size();
        for(int i=0;i<n;i++)
        {
            my_queue.push(popped[i]);
            smulate_stack.push(pushed[i]);
            while(!smulate_stack.empty()&&smulate_stack.top()==my_queue.front())
            {#前面每次都会push,smulate_stack应该都不会empty()的，为什么不加empty就不行呢？
                my_queue.pop();
                smulate_stack.pop();
            }
        }
        
        if(my_queue.empty())
        {
            return true;
        }
        else{return false;}        
    }
};
