#include <stdio.h>
#include <stdlib.h>
#include "numbers.h"

void huge_add_huge(int** digits_ptr, int* size_ptr, int* huge, int huge_size)
{
    int carry = 0;
    int i;

    for (i = 1; i < *size_ptr + 1; i++)
    {
        int temp = (*digits_ptr)[*size_ptr - i];

        if (i <= huge_size)
        {
            temp += huge[huge_size - i];
        }

        if (carry != 0)
        {
            temp += 1;
            carry = 0;
        }

        if (temp >= 10)
        {
            carry = 1;
            temp = temp - 10;
        }

        (*digits_ptr)[*size_ptr - i] = temp;
    }

    if (carry != 0)
    {
        *size_ptr += 1;
        int* new_array = (int*)malloc(*size_ptr * sizeof(int));
        new_array[0] = 1;

        for (i = 1; i < *size_ptr; i++)
        {
            new_array[i] = (*digits_ptr)[i - 1];
        }

        *digits_ptr = new_array;
    }
}

/*
 * This function will only work if multiple is a single digit number.
 */
void huge_multiply_int(int** digits_ptr, int* size_ptr, int multiple)
{
    int carry = 0;
	int i;

	for (i = *size_ptr - 1; i >= 0; i--)
	{
		int temp = (*digits_ptr)[i] * multiple;

		if (carry != 0)
		{
			temp += carry;
			carry = 0;
		}

		if (temp >= 10)
		{
			carry = temp / 10;
			temp = temp - 10;
		}

		(*digits_ptr)[i] = temp;
	}

	if (carry != 0)
	{
		*size_ptr += 1;
		int* new_array = (int*)malloc(*size_ptr * sizeof(int));
		new_array[0] = carry;

		for (i = 1; i < *size_ptr; i++)
		{
			new_array[i] = (*digits_ptr)[i - 1];
		}

		*digits_ptr = new_array;
	}
}

void print_huge(int* huge, int size)
{
	for (int i = 0; i < size; i++)
	{
		printf("%d", huge[i]);
	}

	printf("\n");
}
