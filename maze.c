#include <stdio.h>
#include <stdlib.h>
#include "maze.h"

int main(int argc, char *argv[])
{
    // Check arguments on the command line
    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s <maze_file>\n", argv[0]);
        return 1;
    }

    // Initialize maze structure
    Maze maze;

    // Load maze files
    if (load_maze(&maze, argv[1]) != 0)
    {
        fprintf(stderr, "Failed to load maze.\n");
        return 1;
    }

    // Core game loop
    char input;
    while (1)
    {
        scanf(" %c", &input); // ignore blank characters

        // Quit command
        if (input == 'q' || input == 'Q')
        {
            break;
        }
        // Display command
        else if (input == 'm' || input == 'M')
        {
            display_maze(&maze);
        }
        // Movement command (W/A/S/D)
        else
        {
            move_player(&maze, input);
        }
    }
    return 0;
}

// Load maze from text file, 0 on success, -1 on error
int load_maze(Maze *maze, const char *filename)
{
    // TODO:
    // 1. Using fopen() to open file
    // 2. Validate size (5 <= width/height <= 100)
    // 3. Recognize command 'S' (start) and 'E' (exit)
    return 0;
}

// Handle player's movement command
void move_player(Maze *maze, char direction)
{
    // TODO:
    // 1. Calculate new position
    // 2. Check boundary condition (walls/boundaries)
    // 3. Update new position
}

// Display current situation
void display_maze(const Maze *maze)
{
    // TODO:
    // 1. Traverse the whole maze
    // 2. Display 'X' at player's position
}
