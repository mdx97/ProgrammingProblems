/*
 * Author: Mathew Horner
 * File: Problem 28 (Number Spiral Diagonals)
 * Description: Creates a number spiral and adds up the digits in the two diagonal sections of the grid.
 */
#include <stdio.h>
#include <stdlib.h>

const int GRID_SIZE = 1001;

int main(int argc, char* argv[])
{
    // Allocate memory for grid.
    int** grid = (int**)malloc(GRID_SIZE * sizeof(int *));
    int i;

    for (i = 0; i < GRID_SIZE; i++)
    {
        grid[i] = (int*)malloc(GRID_SIZE * sizeof(int));
    }

    // Start position for filling.
    int x = GRID_SIZE / 2;
    int y = x;

    grid[y][x] = 1;

    // Fill in the rest of the spiral
    int dir = 1;
    int step = 1;
    int iter = 2;
    int count = 0;
    int step_count = 0;

    while (1)
    {
        if (x == (GRID_SIZE - 1) && y == 0)
        {
            break;
        }

        switch (dir)
        {
            // Right
            case 1:
                x += 1;
                break;
            
            // Down
            case 2:
                y += 1;
                break;

            // Left
            case 3:
                x -= 1;
                break;
            
            // Up
            case 4:
                y -= 1;
                break;
        }

        grid[y][x] = iter;
        iter++;
        count++;

        if (count == step)
        {
            count = 0;
            dir++;

            if (dir == 5)
            {
                dir = 1;
            }

            step_count++;

            // Only move a certain "step" 2 times.
            if (step_count == 2)
            {
                step++;
                step_count = 0;
            }
        }
    }

    long diag_sum = 0;

    for (i = 0; i < GRID_SIZE; i++)
    {
        diag_sum += grid[i][i];
        diag_sum += grid[GRID_SIZE - i - 1][i];
    }

    // Subtract 1 since we only need to add the intersection once
    diag_sum -= 1;

    free(grid);
    printf("Sum: %ld\n", diag_sum);
    return 0;
}