class Solution {
public:
	void sortColors(vector<int>& nums) {
		int len = nums.size();
		int left = 0;
		int right = len - 1;
		int tag;
		while (left<right)
		{
			tag = false;
			if (nums[left] == 2 && nums[right] == 0)
			{
				swap(nums[left], nums[right]);
			}
			if (nums[left] == 2 && nums[right] == 1)
			{	
				if (right - left == 1){ swap(nums[left], nums[right]); }
				else{
					for (int k = right - 1; k > left; k--)
					{
						if (nums[k] == 0)
						{
							swap(nums[right], nums[k]);
							swap(nums[right], nums[left]);
							break;
						}
						else if (k == left + 1)
						{
							swap(nums[right], nums[left]);
							break;
						}
					}
				}
			
			}
			if (nums[left] == 2 && nums[right] == 2)
			{
				right--;
				continue;
			}

			if (nums[left] == 1 && nums[right] == 2)
			{				
					for (int k = left + 1; k < right; k++)
					{
						if (nums[k] == 0)
						{
							swap(nums[k], nums[left]);
							break;
						}
					}				
			}
			if (nums[left] == 1 && nums[right] == 1)
			{
				if (right - left == 1) { swap(nums[left], nums[right]); }
				else{
					for (int k = right - 1; k > left; k--)
					{
						if (nums[k] == 2)
						{
							swap(nums[k], nums[right]);
							right--;
							tag = true;
							break;
						}
						else if (nums[k] == 0)
						{
							swap(nums[k], nums[left]);
							tag = true;
							left++;
							break;
						}					
					}
					if (tag){ continue; }
				}
				
			}
			if (nums[left] == 0 && nums[right] == 1)
			{
				
				
					for (int k = right - 1; k > left; k--)
					{
						if (nums[k] == 2)
						{
							swap(nums[k], nums[right]);
							break;
						}
					}
				
			}
			if (nums[left] == 1 && nums[right] == 0)
			{
				if (right - left == 1){ swap(nums[left], nums[right]); }
				else {
					for (int k = right - 1; k > left; k--)
					{
						if (nums[k] == 2)
						{
							swap(nums[k], nums[right]);
							swap(nums[k], nums[left]);
							break;
						}
						else if (k == left + 1)
						{
							swap(nums[left], nums[right]);
							break;
						}
					}
				}
			
			}
			if (nums[left] == 0 && nums[right] == 0)
			{
				left++; continue;
			}
			left++; right--;
		}
	}
	void swap(int &a, int &b)
	{
		int temp = a;
		a = b;
		b = temp;
	}

};
