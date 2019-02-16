/*
 * Author: Mathew Horner
 * File: Problem 12 (Highly Divisble Triangle Number)
 * Description: Finds the first triangle number with over 500 divisors
 */
#include <stdio.h>
#include <math.h>

int count_divisors(int number);
int get_triangle_number(int number);

int main(int argc, char* argv[])
{
	int value = 0;
	int iter = 1;
	int triangle = 1;
	int divisors;

	while (value == 0)
	{
		if (count_divisors(triangle) > 500)
		{
			value = triangle;
		}
		
		iter++;
		triangle = get_triangle_number(iter);
	}

	printf("Number: %d\n", value);
	return 0;
}

int count_divisors(int number)
{
	int count = 1;

	if (number > 1)
	{
		// Set count to 2 for 1 and n.
		count = 2;

		for (int i = 2; i <= sqrt(number); i++)
		{
			if (number % i == 0)
			{
				count += 2;
			}
		}
	}

	return count;
}

int get_triangle_number(int number)
{
	int sum = 0;

	for (int i = 1; i <= number; i++)
	{
		sum += i;
	}

	return sum;
}
