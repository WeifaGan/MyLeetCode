class Solution {
public:
	vector<int> twoSum(vector<int>& nums, int target) {
		map<int, int>TS;
		vector<int>res;
		for (int i = 0; i < nums.size(); i++)
		{
			pair<int, int>item(nums[i], i);
			TS.insert(item);
		}

		for (int i = 0; i < nums.size(); i++)
		{
			int search = target-nums[i] ;
			if (TS.find(search) != TS.end() && i != TS[search])
			{
				res.push_back(i);
				res.push_back(TS[search]);
				break;
			}
		}
		return res;
	}

};
