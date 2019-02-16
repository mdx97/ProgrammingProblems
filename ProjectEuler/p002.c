/*
 * Author: Mathew Horner
 * File: Problem 2 (Even Fibonacci numbers)
 * Description: Gets the sum of the numbers of a Fibonacci sequence that has values not exceeding 4 million.
 */
#include <stdio.h>

unsigned const int MAX = 4000000;

int main(int argc, char* argv[])
{
	int prev = 1;
	int num = 1;
	int sum = 0;
	int temp = 0;

	while (num < MAX)
	{
		temp = num;
		num = num + prev;
		prev = temp;
		
		if (num % 2 == 0)
		{
			sum += num;
		}
	}

	printf("Sum: %d\n", sum);
	return 0;
}
