#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

typedef struct {
    bool visited, blocked;
} coordinate;

typedef struct {
    size_t height;
    coordinate **coordinates;
} map;

typedef struct {
    int x, y;
} guard;

void safe_exit(map *current_map, int code) {
    if (current_map != NULL) {
        for (int i = 0; i < current_map->height - 1; i++) free(current_map->coordinates[i]);
        free(current_map);
    }
    exit(code);
}

void turn_right(guard *direction) {
    if (direction->x == 0 && direction->y == -1) {
        direction->x = 1;
        direction->y = 0;
    } else if (direction->x == 1 && direction->y == 0) {
        direction->x = 0;
        direction->y = 1;
    } else if (direction->x == 0 && direction->y == 1) {
        direction->x = -1;
        direction->y = 0;
    } else {
        direction->x = 0;
        direction->y = -1;
    }
}

bool add_line(map *current_map, char *line, size_t line_length, int *guard_pos) {
    coordinate **new_coordinates = realloc(current_map->coordinates, ++(current_map->height) * sizeof(coordinate*));
    if (new_coordinates == NULL) safe_exit(current_map, -1);
    current_map->coordinates = new_coordinates;
    coordinate *new_line = malloc(line_length * sizeof(coordinate));
    current_map->coordinates[current_map->height - 1] = new_line;
    bool guard_found = false;
    for (int i = 0; i < line_length-1; i++) {
        (new_line+i)->visited = false;
        (new_line+i)->blocked = *(line+i) == '#';
        if (*(line+i) == '^') {
            *guard_pos = i;
            guard_found = true;
        }
    }
    return guard_found;
}

int main(){
	FILE *input_file=fopen("input.txt", "r"), *output_file= fopen("out.txt", "w");
    map *coordinate_map = calloc(sizeof(map), 1);
    guard guard_pos = {0,0};
    char* line = NULL;
    size_t size = 0, len = getline(&line, &size, input_file), saved_len;
    for (int y = 0; len != -1; y++) {
        saved_len = len;
        if (add_line(coordinate_map, line, len, &(guard_pos.x))) guard_pos.y = y;
        len = getline(&line, &size, input_file);
    }
    int visited = 0;
    guard direction = {0, -1};
    while (guard_pos.x > 0 && guard_pos.x < saved_len && guard_pos.y > 0 && guard_pos.y < coordinate_map->height){
        bool *already_visited = &(coordinate_map->coordinates[guard_pos.y][guard_pos.x].visited);
        if (!(*already_visited)) {
            *already_visited = true;
            visited++;
        }
        for (int y = 0; y < coordinate_map->height; y++) {
            for (int x = 0; x < saved_len; x++) {
                if (guard_pos.x == x && guard_pos.y == y) {
                    if (direction.x == 0 && direction.y == -1) {
                        fprintf(output_file, "^");
                    } else if (direction.x == 1 && direction.y == 0) {
                        fprintf(output_file, ">");
                    } else if (direction.x == 0 && direction.y == 1) {
                        fprintf(output_file, "v");
                    } else {
                        fprintf(output_file, "<");
                    }
                } else if (coordinate_map->coordinates[y][x].visited) fprintf(output_file, "X");
                else if (coordinate_map->coordinates[y][x].blocked) fprintf(output_file, "#");
                else fprintf(output_file, ".");
            }
            fprintf(output_file, "\n");
        }
        fprintf(output_file, "%d\n\n-------------------------\n", visited);
        if (!(guard_pos.x + direction.x >= 0 && guard_pos.x + direction.x < saved_len && guard_pos.y + direction.y >= 0 && guard_pos.y + direction.y < coordinate_map->height)) break;
        if (coordinate_map->coordinates[guard_pos.y+direction.y][guard_pos.x+direction.x].blocked) turn_right(&direction);
        guard_pos.x += direction.x;
        guard_pos.y += direction.y;
    }
    int second_counter = 0;
    for (int y = 0; y < coordinate_map->height; y++) {
        for (int x = 0; x < saved_len; x++) {
            second_counter += coordinate_map->coordinates[y][x].visited;
        }
    }
    fprintf(output_file, "\n\n\n%d", second_counter);
    safe_exit(coordinate_map, 0);
}
