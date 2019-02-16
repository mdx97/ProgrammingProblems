/*
 * Author: Mathew Horner
 * File: Problem 1 (Multiples of 3 and 5)
 * Description: Finds the sum of all multiples of 3 and 5 below 1000.
 */
#include <stdio.h>

const int LIMIT = 1000;

int main(int argc, char* argv[])
{
	int sum = 0;

	for (int i = 0; i < LIMIT; i++)
	{
		if ((i % 3 == 0) || (i % 5 == 0))
		{
			sum += i;
		}
	}

	printf("Sum: %d", sum);
	return 0;
}
