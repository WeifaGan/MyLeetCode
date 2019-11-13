class Solution {
	public:
		vector<vector<int>> subsets(vector<int>& nums) {
			int len = nums.size();
			int start = 0;
			vector<vector<int>> list;
			vector<int> templist;
			traceback(start, len, list, templist, nums);
			return list;
		}

		void traceback(int start, int len, vector<vector<int>>&list, vector<int> templist, vector<int>&nums)
		{
			list.push_back(templist);
			for (int i = start; i<len; i++)
			{
				templist.push_back(nums[i]);
				traceback(++i, len, list, templist, nums);
				templist.pop_back();
			}
		}
	};
