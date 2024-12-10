#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct {
    int **lines;
    int size;
} map;

void safe_exit(map *topo_map, int code) {
    for (int i = 0; i < topo_map->size; ++i) free(topo_map->lines[i]);
    free(topo_map->lines);
    exit(code);
}

size_t find_trails(map topo_map, size_t line_length, int current_x, int current_y) {
    int current_val = topo_map.lines[current_y][current_x];
    if (current_val == 9) return 1;
    int x_candidates[4] = {-1, 0, 0, 1};
    int y_candidates[4] = {0, 1, -1, 0};
    size_t current = 0;
    for (int i = 0; i < 4; i++) {
        int x_candidate = current_x + x_candidates[i];
        int y_candidate = current_y + y_candidates[i];
        if (x_candidate >= 0 && x_candidate < line_length && y_candidate >= 0 && y_candidate < topo_map.size &&
            topo_map.lines[y_candidate][x_candidate] == current_val + 1)
            current += find_trails(topo_map, line_length, x_candidate, y_candidate);
    }
    return current;
}

int main() {
    FILE *input_file = fopen("input.txt", "r");
    map topo_map = {malloc(0), 0};
    char *line = NULL;
    size_t size, len = getline(&line, &size, input_file), saved_len, trailheads = 0;
    while (len != -1) {
        int **new_lines = reallocarray(topo_map.lines, ++(topo_map.size), sizeof(int *));
        if (new_lines == NULL) safe_exit(&topo_map, -1);
        topo_map.lines = new_lines;
        saved_len = len - 1;
        int *new_line = calloc(saved_len, sizeof(int));
        topo_map.lines[topo_map.size - 1] = new_line;
        for (int i = 0; i < saved_len; i++) {
            *(new_line + i) = *(line + i) - '0';
        }
        len = getline(&line, &size, input_file);
    }
    fclose(input_file);
    for (int y = 0; y < topo_map.size; y++)
        for (int x = 0; x < saved_len; x++)
            if (topo_map.lines[y][x] == 0) {
                trailheads += find_trails(topo_map, saved_len, x, y);
            }
    printf("%zu", trailheads);

    safe_exit(&topo_map, 0);
}
