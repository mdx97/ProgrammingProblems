#include <stdio.h>
#include <stdlib.h>
#include "prime.h"

const int MAX = 2000000;

int main(int argc, char* argv[])
{
	int count_primes = 0;
	int* primes = sieve(MAX, &count_primes);
	
	unsigned long long sum = 0;
	
	for (int i = 0; i < count_primes; i++)
	{
		sum += primes[i];
	}
	
	free(primes);
	
	printf("Sum: %lld\n", sum);
	return 0;
}
