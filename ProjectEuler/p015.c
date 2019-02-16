/*
 * Author: Mathew Horner
 * File: Problem 15 (Lattice Paths)
 * Description: Finds the number of lattice paths in a square grid
 */
#include <stdio.h>
#include <stdlib.h>
#include "numbers.h"

const int GRID_SIZE = 20;

BIG get_paths(int x, int y, BIG** paths);

int main(int argc, char* argv[])
{
	// Allocate a matrix to cache results for the algorithm
	BIG** paths;
	paths = malloc((GRID_SIZE + 1) * sizeof(BIG *));
	
	int i, j;

	// Initialize the paths matrix with -1 for all values
	for (i = 0; i < GRID_SIZE + 1; i++)
	{
		paths[i] = malloc((GRID_SIZE + 1) * sizeof(BIG));

		for (j = 0; j < GRID_SIZE + 1; j++)
		{
			paths[i][j] = -1;
		}
	}
	
	// Calculate paths starting at the origin of the grid
	BIG count = get_paths(0, 0, paths);
	printf("Count paths: %llu\n", count);
	
	// Free memory
	for (i = 0; i < GRID_SIZE + 1; i++)
	{
		free(paths[i]);
	}

	free(paths);

	return 0;
}

BIG get_paths(int x, int y, BIG** paths)
{
	// Use memoization to optimize the algorithm
	if (paths[x][y] != -1)
	{
		return paths[x][y];
	}

	if (x == GRID_SIZE && y == GRID_SIZE)
	{
		return 1;
	}

	// Recursively count paths
	BIG count = 0;

	if (x < GRID_SIZE)
	{
		count += get_paths(x + 1, y, paths);
	}

	if (y < GRID_SIZE)
	{
		count += get_paths(x, y + 1, paths);
	}
	
	// Cache result
	paths[x][y] = count;

	return count;
}
