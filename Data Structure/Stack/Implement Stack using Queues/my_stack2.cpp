class MyStack {
private: 
    queue<int>my_queue;
public:
    /** Initialize your data structure here. */
    MyStack() {
     
    }
    
    /** Push element x onto stack. */
    void push(int x) {
     queue<int>temp_queue;
        temp_queue.push(x);
        while(!my_queue.empty())
        {
            temp_queue.push(my_queue.front());
            my_queue.pop();
        }
        my_queue = temp_queue;
        
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
     int pop_element = my_queue.front();   
     my_queue.pop();
    return pop_element;
        
    }
    
    /** Get the top element. */
    int top() {
        return my_queue.front();
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
