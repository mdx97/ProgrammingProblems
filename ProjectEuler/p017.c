/*
 * Author: Mathew Horner
 * File: Problem 17 (Number letter counts)
 * Description: Finds the sum of the number of letters of each number 1-1000
 */
#include <stdio.h>
#include <stdlib.h>

// Letter counts for 1 - 9
const int DIGIT_LETTER_COUNTS[] = {3, 3, 5, 4, 4, 3, 5, 5, 4};

// Letter counts for 11 - 19
const int TEEN_LETTER_COUNTS[] = {6, 6, 8, 8, 7, 7, 9, 8, 8};

// Letter counts for 10, 20 ... 90
const int TENS_LETTER_COUNTS[] = {3, 6, 6, 5, 5, 5, 7, 6, 6};

// Single value constants
const int HUNDRED_LETTER_COUNT = 7;
const int THOUSAND_LETTER_COUNT = 8;
const int AND_LETTER_COUNT = 3;

// Number the algorithm will stop at
const int MAX = 1000;

int number_letter_count(int num);
int digit_count(int num);

int main(int argc, char* argv[])
{
	long sum = 0;

	for (int i = 1; i <= MAX; i++)
	{
		sum += number_letter_count(i);
	}

	printf("Sum: %d\n", sum);
	return 0;	
}

int number_letter_count(int num)
{
	// Get the number of digits in the number
	int len = digit_count(num);

	// Create an integer array to store the digits of the number
	int* digits = (int *)malloc(len * sizeof(int));
	int* ptr = digits + len - 1;

	while (num > 0)
	{
		*ptr = num % 10;
		num /= 10;
		ptr -= 1;
	}

	// Count the letters in the number
	int letter_count = 0;
	int iter = 0;
	int has_teen = 0;
	int has_ten = 0;
	
	while (iter < len)
	{
		int digit = digits[iter];

		if (digit > 0)
		{
			if (len - iter == 4)
			{
				// Thousands digit
				letter_count += (DIGIT_LETTER_COUNTS[digit - 1] + THOUSAND_LETTER_COUNT);
			} 
			else if (len - iter == 3)
			{
				// Hundreds digit
				letter_count += (DIGIT_LETTER_COUNTS[digit - 1] + HUNDRED_LETTER_COUNT);
			} 
			else if (len - iter == 2)
			{
				// Tens digit
				// Add "and" if the number has digits greater than tens
				if (letter_count != 0)
				{
					letter_count += AND_LETTER_COUNT;
				}

				if (digit == 1)
				{
					// Teen number
					int next_digit = digits[iter + 1];

					if (next_digit == 0)
					{
						letter_count += TENS_LETTER_COUNTS[0];
					}
					else
					{
						letter_count += TEEN_LETTER_COUNTS[next_digit - 1];
					}

					has_teen = 1;
				}
				else
				{
					// Tens digit
					letter_count += TENS_LETTER_COUNTS[digit - 1];
					has_ten = 1;
				}
			} 
			else if ((len - iter == 1) && (has_teen == 0))
			{
				// If needed, add "and"
				if (letter_count != 0 && has_ten == 0)
				{
					letter_count += AND_LETTER_COUNT;
				}

				// Single digit
				letter_count += DIGIT_LETTER_COUNTS[digit - 1];
			}
		}

		iter++;
	}

	free(digits);
	return letter_count;
}

int digit_count(int num)
{
	int count = 0;
	
	while (num > 0)
	{
		num /= 10;
		count++;
	}

	return count;
}
