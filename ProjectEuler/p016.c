#include <stdio.h>
#include <stdlib.h>
#include "numbers.h"

void print_array(int* arr, int size);

int main(int argc, char* argv[])
{
	int i;
	int* huge = (int*)malloc(sizeof(int));
	int count = 1;
	*huge = 2;

	for (i = 0; i < 999; i++)
	{
		huge_multiply_int(&huge, &count, 2);
	}

	int sum = 0;

	for (i = 0; i < count; i++)
	{
		sum += huge[i];
	}

	free(huge);
	printf("Power digit sum: %d\n", sum);
	return 0;
}