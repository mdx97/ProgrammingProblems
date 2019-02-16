#include <stdlib.h>

int get_max(int num1, int num2);

// This function utilizes Dynamic Programming to find the maximum path.
int maximum_path_sum(int **triangle, int triangle_size)
{
	int i, j;
	int **lookup_table = calloc(triangle_size, sizeof(int *));

	for (i = 0; i < triangle_size; i++)
		lookup_table[i] = calloc(triangle_size, sizeof(int));
	
	lookup_table[0][0] = triangle[0][0];

	for (i = 1; i < triangle_size; i++)
	{
		for (j = 0; j < triangle_size; j++)
		{
			if (j > 0)
			{
				// Check the locally optimal values directly above and above and to the left of the number.
				// Take the higher of these two values and add it to the current number to get the maximum path at this position. 
				int max_path = get_max(lookup_table[i - 1][j], lookup_table[i - 1][j - 1]);
				lookup_table[i][j] = triangle[i][j] + max_path;
			}
			else
			{
				// This number is at the far left of the triangle, so we can only use the value directly above to determine the maximum path at this position. 
				lookup_table[i][j] = triangle[i][j] + lookup_table[i - 1][j];
			}
		}
	}

	int bottom_row_max = 0;

	for (i = 0; i < triangle_size; i++)
	{
		if (lookup_table[triangle_size - 1][i] > bottom_row_max)
			bottom_row_max = lookup_table[triangle_size - 1][i];
	}

	return bottom_row_max;
}

int get_max(int num1, int num2)
{
	if (num1 > num2)
		return num1;
	else
		return num2;
}
