class MyQueue {
private:
    stack<int> mystack;
public:
    /** Initialize your data structure here. */
    MyQueue() {
        
    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        stack<int>tmp_mystack;
        while(!mystack.empty())
        {
            tmp_mystack.push(mystack.top());
            mystack.pop();
        }
        mystack.push(x);
        while(!tmp_mystack.empty())
        {
            mystack.push(tmp_mystack.top());
            tmp_mystack.pop();
        }
        
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        int elem=mystack.top();
       mystack.pop();
        return elem;
    }
    
    /** Get the front element. */
    int peek() {
        return mystack.top();
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return mystack.empty();
    }
};
