class Solution {
public:
	vector<vector<int>> permuteUnique(vector<int>& nums) {
		vector<int>templist;
		vector<bool>visited(nums.size(), false);
		vector<vector<int>>list;
		sort(nums.begin(), nums.end());
		backtrace(list, templist, nums, visited);
		return list;

	}

	void backtrace(vector<vector<int>>&list, vector<int>templist, vector<int>nums, vector<bool> visited)
	{
		if (templist.size() == nums.size()) list.push_back(templist);
		
		for (int i = 0; i<nums.size(); i++)
		{
			
			if (visited[i]){ continue; }
			
			if (i>0 && nums[i] == nums[i - 1]&&visited[i-1]){ continue; }
			visited[i] = true;
			templist.push_back(nums[i]);
			backtrace(list, templist, nums, visited);
			templist.pop_back();
			visited[i] = false;
		}
	}
};
