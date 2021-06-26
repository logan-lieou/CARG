#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// height and width of the grid
#define HEIGHT 20
#define WIDTH  20

int random_int(int lower, int upper)
{
	return (rand() % (upper - lower) + 0) + lower;
}

void print_grid(int grid[HEIGHT][WIDTH]) {
	for (int i = 0; i < HEIGHT; i++) {
		for (int j = 0; j < WIDTH; j++) {
			printf("%d", grid[i][j]);
		}
		printf("\n");
	}
}

int main()
{
	int grid[HEIGHT][WIDTH];

	srand(time(0));

	for (int i = 0; i < HEIGHT; i++) {
		for (int j = 0; j < WIDTH; j++) {
			grid[i][j] = random_int(0, 2);
		}
	}

	print_grid(grid);
}
