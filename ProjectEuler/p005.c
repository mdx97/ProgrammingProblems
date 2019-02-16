/*
 * Author: Mathew Horner
 * File: Problem 5 (Smallest multiple)
 * Description: Finds the smallest integer that is evenly divisible by all numbers between 1 and 20.
 */
#include <stdio.h>

int main(int argc, char* argv[])
{
	int smallest = 0;
	int number = 0;

	while (smallest == 0)
	{
		int divisible_by_all = 1;

		for (int i = 1; i <= 20; i++)
		{
			if (number % i != 0)
			{
				divisible_by_all = 0;
			}
		}

		if (divisible_by_all == 1)
		{
			smallest = number;
		}

		// Only check even numbers.
		number += 2;
	}

	printf("Smallest multiple: %d\n", smallest);
	return 0;
}
