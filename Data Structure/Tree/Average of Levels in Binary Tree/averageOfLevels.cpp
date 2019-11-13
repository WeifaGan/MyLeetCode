class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
     deque<TreeNode*> de_node;
     vector<double>vec_val;
     if (root==NULL)return vec_val;
     de_node.push_back(root);
     while(!de_node.empty())
     {
        int size=de_node.size();
         int sc=size;
        double sum=0;
         while(size>0)
         {
             TreeNode* node=de_node.front();
             if(node->left)
             {de_node.push_back(node->left);}
             if(node->right)
             {de_node.push_back(node->right);}
             
             sum+=node->val;
             de_node.pop_front();
             size--;
         }
         vec_val.push_back(double(sum)/sc);    
     }
    return vec_val;
}};
