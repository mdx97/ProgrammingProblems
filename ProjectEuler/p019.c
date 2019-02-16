/*
 * Author: Mathew Horner
 * File: Problem 19 (Counting Sundays)
 * Description: Finds how many months in the 20th century began with a Sunday.
 */
#include <stdio.h>

const int MONTH_DAY_COUNTS[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
const int START_YEAR = 1901;
const int START_YEAR_DAYOFWEEK = 3;
const int END_YEAR = 2001;

int main(int argc, char* argv[])
{
	int count = 0;

	int day_of_week = START_YEAR_DAYOFWEEK;
	int month = 0;
	int year = START_YEAR;

	while (year < END_YEAR)
	{
		if (day_of_week == 1)
		{
			count++;
		}

		int days_to_add = MONTH_DAY_COUNTS[month];

		// Month is February and year is divisible by 4.
		if (month == 1 && year % 4 == 0)
		{
			// A leap year does not occur on a century unless the century is divisible by 400.
			if (year % 100 != 0 || year % 400 == 0)
			{
				days_to_add++;
			}
		}

		day_of_week = (day_of_week + MONTH_DAY_COUNTS[month]) % 7;
		
		if (month == 11)
		{
			month = 0;
			year++;
		}
		else
		{
			month++;
		}
	}

	printf("Sundays on 1st of Month: %d\n", count);
	return 0;
}
