class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
    vector<vector<int>>list;
    vector<int>templist;
    PreOrder(list,templist,root,sum);
    return list;
        
    }
    
   void PreOrder(vector<vector<int>> &list,vector<int> templist,TreeNode* root,int remain)
    {
        if(root!=NULL)
        {
            templist.push_back(root->val);
            remain=remain-root->val;
            if(remain==0&&root->left==NULL&&root->right==NULL)
            {list.push_back(templist);}
            PreOrder(list,templist,root->left,remain);
            PreOrder(list,templist,root->right,remain);
        }
    }
};
