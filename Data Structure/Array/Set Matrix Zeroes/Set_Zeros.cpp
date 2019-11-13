class Solution {
public:
	void setZeroes(vector<vector<int>>& matrix) {
		int leny = matrix.size();
		int lenx = matrix[0].size();
		bool firstrow = false;
		bool firstcol = false;
		for (int i = 0; i<leny; i++)
		{
			for (int j = 0; j<lenx; j++)
			{
				if (i == 0 && matrix[i][j] == 0)
					firstrow = true;
				if (j == 0 && matrix[i][j] == 0)
					firstcol = true;
				if (i != 0 && j != 0 && matrix[i][j] == 0)
				{
					matrix[0][j] = 0;
					matrix[i][0] = 0;
				}
			}
		}

		for (int i = 1; i<leny; i++)
		{
			for (int j = 1; j<lenx; j++)
			{
				if (matrix[i][0]==0 || matrix[0][j]==0)
				{
					matrix[i][j] = 0;
				}
			}
		}
		if (firstrow)
		{
			for (int k= 0; k < lenx; k++)
			{
				matrix[0][k] = 0;
			}
		}

		if (firstcol)
		{
			for (int k = 0; k < leny; k++)
			{
				matrix[k][0] = 0;
			}
		}


	}
};
