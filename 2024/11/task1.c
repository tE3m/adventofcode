#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main() {
    FILE *input_file = fopen("input.txt", "r");
    char *line = NULL;
    size_t previous_size = 0, current_size, len;
    current_size = getline(&line, &len, input_file);
    fclose(input_file);
    long *previous_line = malloc(0), *current_line;
    for (char *pos = line; pos < line + current_size - 1; previous_size++) {
        long *new_ptr = reallocarray(previous_line, previous_size + 1, sizeof(long));
        if (new_ptr == 0) exit(-1);
        previous_line = new_ptr;
        previous_line[previous_size] = strtol(pos, &pos, 10);
    }
    free(line);
    for (int i = 0; i < 25; i++) {
        current_line = malloc(previous_size * 2 * sizeof(long));
        current_size = 0;
        for (int pos = 0; pos < previous_size; pos++) {
            long previous_val = previous_line[pos];
            if (previous_val == 0) current_line[current_size++] = 1;
            else {
                int digit_count = (int) log10(previous_val) + 1;
                if (!(digit_count % 2)) {
                    int half_digit_power = (int) pow(10, digit_count / 2);
                    current_line[current_size++] = previous_val / half_digit_power;
                    current_line[current_size++] = previous_val % half_digit_power;
                } else current_line[current_size++] = previous_val * 2024;
            }
        }
        long *current_line_short = reallocarray(current_line, current_size, sizeof(long));
        if (current_line_short == NULL) {
            free(previous_line);
            free(current_line);
            exit(-1);
        }
        free(previous_line);
        previous_line = current_line_short;
        previous_size = current_size;
    }
    printf("%ld", previous_size);
    free(previous_line);

}
