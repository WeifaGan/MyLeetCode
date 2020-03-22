class MyStack {
private: 
    queue<int>my_queue;
public:
    /** Initialize your data structure here. */
    MyStack() {
     
    }
    
    /** Push element x onto stack. */
    void push(int x) {
        my_queue.push(x);
        
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        queue<int> my_queue1;
        while(!my_queue.empty()&&my_queue.size()>1)
        {   
            int element = my_queue.front();
            my_queue1.push(element);
            my_queue.pop();
        }
        int pop_element = my_queue.front();
        my_queue.pop();
        my_queue = my_queue1;
        return pop_element;
        
        
    }
    
    /** Get the top element. */
    int top() {
        return my_queue.back();
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
    return my_queue.empty();        
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
