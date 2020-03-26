**性质**  
* 堆是一个最大(小)值先出的完全二叉树
* 最大堆的子节点的值都比父节点的值要大
* 最小堆的子节点的值都比父节点的值要小

**声明**  
* 最大堆 priority_queue<int>q
* 最小堆 priority_queue<int,vector<int>,greater<int>> q

**常用操作**  
* heap.top() 返回堆顶元素
* heap.empty() 是否为空
* heap.push(x) 元素x进堆
* heap.pop() 堆顶元素出堆
