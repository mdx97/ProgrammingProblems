#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "triangle.h"

void read_triangle(const char *file_path, int **triangle, int size);

int main(int argc, char *argv[])
{
	const char *FILE_PATH = "files/p067_triangle.txt";
	const int TRIANGLE_SIZE = 100;

	int **triangle = calloc(TRIANGLE_SIZE, sizeof(int *));
	for (int i = 0; i < TRIANGLE_SIZE; i++)
		triangle[i] = calloc(TRIANGLE_SIZE, sizeof(int));

	read_triangle(FILE_PATH, triangle, TRIANGLE_SIZE);

	int out = maximum_path_sum(triangle, TRIANGLE_SIZE);
	printf("Maximum Path Sum: %d\n", out);
	
	return 0;
}

void read_triangle(const char *file_path, int **triangle, int size)
{
	FILE *file_ptr;
	char *line = NULL;
	size_t length = 0;

	file_ptr = fopen(file_path, "r");
	
	int row = 0;
	int col = 0;
	
	while (row < size)
	{
		getline(&line, &length, file_ptr);
		char *new_str = strtok(line, " ");
		
		while (new_str != NULL)
		{
			int num = atoi(new_str);
			triangle[row][col] = num;
			new_str = strtok(NULL, " ");
			col++;
		}

		row++;
		col = 0;
	}
}
