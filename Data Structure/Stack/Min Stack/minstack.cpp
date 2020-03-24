class MinStack {
private:
    stack<int>mystack;
    stack<int>minstack;
public:
    /** initialize your data structure here. */
    MinStack() {
        
    }
    
    void push(int x) {
      mystack.push(x);
      if(minstack.empty()||x<=minstack.top())#minstack.empty()要放在前面，因为如果是empty的，就不能有top()了
      {minstack.push(x);}
      else{minstack.push(minstack.top());}
        
    }
    
    void pop() {
        mystack.pop();
        minstack.pop();
    }
    
    int top() {
        return mystack.top();
    }
    
    int getMin() {
     return minstack.top();
    }
};
