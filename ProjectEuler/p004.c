/*
 * Author: Mathew Horner
 * File: Problem 4 (Largest Palindrome Product)
 * Description: Finds the largest palindrome number made from the product of two 3 digit numbers
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int is_palindrome_number(int number);

int main(int argc, char* argv[])
{
	int largest = 0;

	for (int i = 100; i < 1000; i++)
	{
		for (int j = 100; j < 1000; j++)
		{
			int product = i * j;

			if (is_palindrome_number(product) == 1)
			{
				if (product > largest)
				{
					largest = product;
				}
			}
		}
	}

	printf("Largest Palindrome: %d\n", largest);
	return 0;
}

int is_palindrome_number(int number)
{
	char str[11];
	itoa(number, str, 10);
	int length = strlen(str);
	int is_palindrome = 1;

	char* forward_ptr = str;
	char* backward_ptr = str + (length - 1);

	for (int i = 0; i < length / 2; i++)
	{
		if (*forward_ptr != *backward_ptr)
		{
			is_palindrome = 0;
		}

		forward_ptr += 1;
		backward_ptr -= 1;
	}

	return is_palindrome;
}
