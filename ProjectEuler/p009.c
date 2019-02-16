/*
 * Author: Mathew Horner
 * File: Problem 9 (Special Pythagorean Triplet)
 * Description: Finds the product of the pythagorean triplet where a + b + c = 1000
 */
#include <stdio.h>

const int MAX = 1000;

int main(int argc, char* argv[])
{
	int product = 0;

	for (int c = 0; c < MAX; c++)
	{
		for (int b = 0; b < c; b++)
		{
			for (int a = 0; a < b; a++)
			{
				// Check if a, b, and c satisfy the Pythagorean theorem
				if ((a * a) + (b * b) == (c * c))
				{
					if ((a + b + c) == 1000)
					{
						product = a * b * c;
					}
				}
			}
		}
	}

	printf("Product: %d\n", product);
	return 0;
}
