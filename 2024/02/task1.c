#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(){
	FILE *input_file=fopen("input.txt", "r");
    size_t linesize = 24;
    int safe = 0;
    char *line = NULL, *pos = NULL;
    while (getline(&line, &linesize, input_file) != -1) {
        long diff, new_diff = 0, dist, first_val, second_val = strtol(line, &pos, 10);
        do {
            diff = new_diff;
            first_val = second_val;
            second_val = strtol(pos, &pos, 10);
            new_diff = first_val - second_val;
            dist = labs(new_diff);
        } while (*pos != '\n' && *pos != '\0' && !(diff < 0 && new_diff > 0 || diff > 0 && new_diff < 0 || dist < 1 || dist > 3));
        safe += (diff < 0 && new_diff > 0 || diff > 0 && new_diff < 0 || dist < 1 || dist > 3) ? 0 : 1;
    }
    free(line);
    printf("%d", safe);
}
