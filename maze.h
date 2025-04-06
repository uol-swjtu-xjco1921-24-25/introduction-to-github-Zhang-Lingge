#ifndef MAZE_H
#define MAZE_H

#define MAX_SIZE 100
#define MIN_SIZE 5

// define the structure of the maze
typedef struct
{
    char grid[MAX_SIZE][MAX_SIZE]; // map content
    int width, height;             // sizde
    int player_x, player_y;        // player's direction
} Maze;

// functions
int load_maze(Maze *maze, const char *filename); // load maze files
void move_player(Maze *maze, char direction);    // player's movement
void display_maze(const Maze *maze);             // display the whole maze

#endif