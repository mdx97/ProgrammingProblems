/*
 * Author: Mathew Horner
 * File: Problem 3 (Largest Prime Factor)
 * Description: Gets the largest prime factor of a number
 */
#include <stdio.h>
#include <math.h>
#include "prime.h"
#include "numbers.h"

const BIG NUMBER = 600851475143;

int main(int argc, char* argv[])
{
	BIG i = sqrt(NUMBER);

	if (i % 2 == 0)
	{
		i -= 1;
	}

	BIG factor = 0;

	while (factor == 0 && i > 0)
	{
		if (NUMBER % i == 0)
		{
			if (is_prime_opt(i))
			{
				factor = i;
			}
		}

		i -= 2;
	}

	printf("Largest factor: %llu\n", factor);
	return 0;
}
