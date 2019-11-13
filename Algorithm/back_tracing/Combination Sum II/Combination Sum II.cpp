class Solution {
public:
	vector<vector<int>> combinationSum2(vector<int>& candidates, int target)
	{

		vector<int> templist;
		vector<vector<int>>list;
		int start = 0;
		sort(candidates.begin(), candidates.end());
		int remain = target;
		backtrace(list, templist, candidates, remain, start);
		return list;

	}
	void backtrace(vector<vector<int>> &list, vector<int>templist, vector<int>candidatates, int remain, int start)
	{
		int p = 0;

		if (remain<0) return;
		if (remain == 0) list.push_back(templist);
		for (int i = start; i<candidatates.size(); i++)
		{
			p++;
			if (p>1 && i - 1 >= 0 && candidatates[i] == candidatates[i - 1]) continue;
			templist.push_back(candidatates[i]);
			backtrace(list, templist, candidatates, remain - candidatates[i], i + 1);
			templist.pop_back();
		}
	}

};
