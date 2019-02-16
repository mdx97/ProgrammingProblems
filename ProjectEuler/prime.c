/*
 * Author: Mathew Horner
 * File: prime.c
 * Description: Function library for prime numbers.
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int is_prime(long number)
{
	int is_prime_number = 0;

	if (number > 1)
	{
		is_prime_number = 1;

		for (long i = 2; i <= number / 2; i++)
		{
			if (number % i == 0)
			{
				is_prime_number = 0;
			}
		}
	}

	return is_prime_number;
}

int is_prime_opt(long number)
{
	int is_prime_number = -1;
	
	if (number == 0 || number == 1 || number % 2 == 0)
	{
		is_prime_number = 0;
	}

	if (number == 2)
	{
		is_prime_number = 1;
	}

	if (is_prime_number == -1)
	{
		is_prime_number = 1;
		long iter = 3;

		while (iter <= number / 2 && is_prime_number == 1)
		{
			if (number % iter == 0)
			{
				is_prime_number = 0;
			}

			iter += 2;
		}
	}

	return is_prime_number;
}

int* sieve(int number, int* count_primes)
{
	int size = number - 2;
	int* numbers = malloc(size * sizeof(int));
	
	for (int i = 0; i < size; i++)
	{
		numbers[i] = 1;
	}
	
	for (int j = 2; j < (int)sqrt(number); j++) 
	{
		if (numbers[j - 2] == 1)
		{
			for (int k = (j * j); k < number; k += j)
			{
				numbers[k - 2] = 0;
			}
		}
	}
	
	*count_primes = 0;
	
	for (int l = 0; l < size; l++)
	{
		if (numbers[l] == 1)
		{
			*count_primes += 1;
		}
	}
	
	int* primes = malloc(*count_primes * sizeof(int));
	int iter = 0;
	
	for (int m = 0; m < size; m++)
	{
		if (numbers[m] == 1)
		{
			primes[iter] = m + 2;
			iter++;
		}
	}
	
	free(numbers);
	
	return primes;
}
