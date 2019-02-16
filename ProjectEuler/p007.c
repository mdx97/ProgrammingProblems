/*
 * Author: Mathew Horner
 * File: Problem 7 (10001st prime)
 * Description: Finds the 10001st prime number.
 */
#include <stdio.h>
#include "prime.h"

const int MAX = 10001;

int main(int argc, char* argv[])
{
	int prime = 0;
	int prime_count = 0;
	int iter = 0;

	while (prime == 0)
	{
		if (is_prime(iter))
		{
			prime_count++;

			if (prime_count == MAX)
			{
				prime = iter;
			}
		}

		iter++;
	}

	printf("Prime #%d: %d\n", MAX, prime);
	return 0;
}
