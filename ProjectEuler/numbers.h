#ifndef NUMBERS_H
#define NUMBERS_H

typedef unsigned long long BIG;

void huge_add_huge(int** digits_ptr, int* size_ptr, int* huge, int huge_size);
void huge_multiply_int(int** digits_ptr, int* size_ptr, int multiple);
void print_huge(int* huge, int size);

#endif