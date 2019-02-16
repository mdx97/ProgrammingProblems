/*
 * Author: Mathew Horner
 * File: Problem 6 (Sum square difference)
 * Description: Finds the difference between the sum of squares of the first one hundred integers and the square of the sum.
 */
#include <stdio.h>

const int MAX = 100;

int main(int argc, char* argv[])
{
	int sum_of_squares = 0;
	int i;

	for (i = 1; i <= MAX; i++)
	{
		sum_of_squares += (i * i);
	}

	int sum = 0;

	for (i = 1; i <= MAX; i++)
	{
		sum += i;
	}

	int squared_sum = sum * sum;
	int diff = squared_sum - sum_of_squares;
	
	printf("Difference: %d\n", diff);
	return 0;
}
