class solusition
{
public:
	int cut_rope(int length)
	{
		if (length < 2)return 0;
		if (length == 2)return 1;
		if (length == 3)return 2;
		int *v = new int[length+1];
		v[0] = 0;
		v[1] = 1;
		v[2] = 2;
		v[3] = 2;
		int max;
		for (int i = 4; i <= length; i++)
		{
			max = 0;
			for (int j = 1; j <=i/2; j++)
			{
				int temp=v[j] * v[i - j];
				if (temp>max)
				{
					max = temp;
				}
			}
			v[i] = max;
		}
		max = v[length];
		delete[] v;
		return max;
	}
};
