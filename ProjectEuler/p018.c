/*
 * Author: Mathew Horner
 * Problem 18 (Maximum Path Sum I)
 * Description: Finds the sum of the path through a triangle with the maximum sum.
 */
#include <stdio.h>
#include <stdlib.h>
#include "triangle.h"

const int TRIANGLE_SIZE = 15;

void initialize_triangle(int **triangle);

int main(int argc, char *argv[])
{
	int **triangle = calloc(TRIANGLE_SIZE, sizeof(int *));

	for (int i = 0; i < TRIANGLE_SIZE; i++)
		triangle[i] = calloc(TRIANGLE_SIZE, sizeof(int));
	
	initialize_triangle(triangle);
	int out = maximum_path_sum(triangle, TRIANGLE_SIZE);
	printf("Maximum Path Sum: %d\n", out);

	return 0;
}

void initialize_triangle(int **triangle)
{
	triangle[0][0] = 75;
	triangle[1][0] = 95;
	triangle[1][1] = 64;
	triangle[2][0] = 17;
	triangle[2][1] = 47;
	triangle[2][2] = 82;
	triangle[3][0] = 18;
	triangle[3][1] = 35;
	triangle[3][2] = 87;
	triangle[3][3] = 10;
	triangle[4][0] = 20;
	triangle[4][1] = 4;
	triangle[4][2] = 82;
	triangle[4][3] = 47;
	triangle[4][4] = 65;
	triangle[5][0] = 19;
	triangle[5][1] = 1;
	triangle[5][2] = 23;
	triangle[5][3] = 75;
	triangle[5][4] = 3;
	triangle[5][5] = 34;
	triangle[6][0] = 88;
	triangle[6][1] = 2;
	triangle[6][2] = 77;
	triangle[6][3] = 73;
	triangle[6][4] = 7;
	triangle[6][5] = 63;
	triangle[6][6] = 67;
	triangle[7][0] = 99;
	triangle[7][1] = 65;
	triangle[7][2] = 4;
	triangle[7][3] = 28;
	triangle[7][4] = 6;
	triangle[7][5] = 16;
	triangle[7][6] = 70;
	triangle[7][7] = 92;
	triangle[8][0] = 41;
	triangle[8][1] = 41;
	triangle[8][2] = 26;
	triangle[8][3] = 56;
	triangle[8][4] = 83;
	triangle[8][5] = 40;
	triangle[8][6] = 80;
	triangle[8][7] = 70;
	triangle[8][8] = 33;
	triangle[9][0] = 41;
	triangle[9][1] = 48;
	triangle[9][2] = 72;
	triangle[9][3] = 33;
	triangle[9][4] = 47;
	triangle[9][5] = 32;
	triangle[9][6] = 37;
	triangle[9][7] = 16;
	triangle[9][8] = 94;
	triangle[9][9] = 29;
	triangle[10][0] = 53;
	triangle[10][1] = 71;
	triangle[10][2] = 44;
	triangle[10][3] = 65;
	triangle[10][4] = 25;
	triangle[10][5] = 43;
	triangle[10][6] = 91;
	triangle[10][7] = 52;
	triangle[10][8] = 97;
	triangle[10][9] = 51;
	triangle[10][10] = 14;
	triangle[11][0] = 70;
	triangle[11][1] = 11;
	triangle[11][2] = 33;
	triangle[11][3] = 28;
	triangle[11][4] = 77;
	triangle[11][5] = 73;
	triangle[11][6] = 17;
	triangle[11][7] = 78;
	triangle[11][8] = 39;
	triangle[11][9] = 68;
	triangle[11][10] = 17;
	triangle[11][11] = 57;
	triangle[12][0] = 91;
	triangle[12][1] = 71;
	triangle[12][2] = 52;
	triangle[12][3] = 38;
	triangle[12][4] = 17;
	triangle[12][5] = 14;
	triangle[12][6] = 91;
	triangle[12][7] = 43;
	triangle[12][8] = 58;
	triangle[12][9] = 50;
	triangle[12][10] = 27;
	triangle[12][11] = 29;
	triangle[12][12] = 48;
	triangle[13][0] = 63;
	triangle[13][1] = 66;
	triangle[13][2] = 4;
	triangle[13][3] = 68;
	triangle[13][4] = 89;
	triangle[13][5] = 53;
	triangle[13][6] = 67;
	triangle[13][7] = 30;
	triangle[13][8] = 73;
	triangle[13][9] = 16;
	triangle[13][10] = 69;
	triangle[13][11] = 87;
	triangle[13][12] = 40;
	triangle[13][13] = 31;
	triangle[14][0] = 4;
	triangle[14][1] = 62;
	triangle[14][2] = 98;
	triangle[14][3] = 27;
	triangle[14][4] = 23;
	triangle[14][5] = 9;
	triangle[14][6] = 70;
	triangle[14][7] = 98;
	triangle[14][8] = 73;
	triangle[14][9] = 93;
	triangle[14][10] = 38;
	triangle[14][11] = 53;
	triangle[14][12] = 60;
	triangle[14][13] = 4;
	triangle[14][14] = 23;
}
