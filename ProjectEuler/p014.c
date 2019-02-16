#include <stdio.h>
#include "numbers.h"

const BIG MAX = 1000000;

BIG collatz_sequence_length(BIG number);

int main(int argc, char* argv[])
{
    BIG longest = 0;
    BIG longest_len = 0;

    for (BIG i = 2; i < MAX; i++)
    {
        BIG length = collatz_sequence_length(i);
        
        if (length > longest_len)
        {
            longest_len = length;
            longest = i;
        }
    }

    printf("Longest Collatz Sequence Start Number: %llu\n", longest);
    return 0;
}

BIG collatz_sequence_length(BIG number)
{
    BIG length = 0;

    while (number > 1)
    {
        if (number % 2 == 0)
        {
            number = number / 2;
        }
        else
        {
            number = (3 * number) + 1;
        }

        length++;
    }

    return length;
}