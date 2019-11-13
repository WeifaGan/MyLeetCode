class Solution {
public:
    vector<int> Level_Travel(TreeNode* root) {
        deque<TreeNode*> vec_node;
        vector<int> vec_val;
        if(root==NULL)return vec_val;
        vec_node.push_back(root);
        TreeNode* node; 
        while(!vec_node.empty())
        {
            node=vec_node.front();  
            if(node->left!=NULL)vec_node.push_back(node->left);
            if(node->right!=NULL)vec_node.push_back(node->right);
            vec_val.push_back(node->val);
            vec_node.pop_front();
 
        }
        
        
        return vec_val;
    }
};
