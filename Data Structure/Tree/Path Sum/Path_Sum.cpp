class Solution {
public:
    bool hasPathSum(TreeNode* root, int sum) {
        if(root==NULL) return false;
        bool flag=false;
        PreOrder(root,sum,flag);
        return flag;
    }
    
    void PreOrder(TreeNode* root,int remain,bool &flag)
    {
        // if(root==NULL)
        if(root!=NULL)
        {
            remain=remain-root->val;
            if(remain==0&&root->left==NULL&&root->right==NULL)
            {
                flag=true;
            }
            PreOrder(root->left,remain,flag);
            PreOrder(root->right,remain,flag);
        }
    
    }
};
