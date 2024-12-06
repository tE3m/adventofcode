#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

bool is_x_mas(char first_char, char second_char, char third_char, char fourth_char, char fifth_char) {
    return first_char == 'M' && second_char == 'S' &&
           third_char == 'A' && fourth_char == 'M' &&
           fifth_char == 'S' ||
           first_char == 'M' && second_char == 'M' &&
           third_char == 'A' && fourth_char == 'S' &&
           fifth_char == 'S' ||
           first_char == 'S' && second_char == 'M' &&
           third_char == 'A' && fourth_char == 'S' &&
           fifth_char == 'M' ||
           first_char == 'S' && second_char == 'S' &&
           third_char == 'A' && fourth_char == 'M' &&
           fifth_char == 'M';
}


int main() {
    FILE *input_file = fopen("input.txt", "r");
    char *first_line, *second_line, *third_line;
    size_t len, remaining = 4;
    int offset, amount = 0;
    getline(&first_line, &len, input_file);
    getline(&second_line, &len, input_file);
    while (getline(&third_line, &len, input_file) != -1) {
        for (offset = 0; *(first_line + offset) != '\n'; offset++) {
            if (offset < len - 2)
                amount += is_x_mas(*(first_line + offset), *(first_line + offset + 2),
                                   *(second_line + offset + 1), *(third_line + offset),
                                   *(third_line + offset + 2));
        }
        free(first_line);
        first_line = second_line;
        second_line = third_line;
        third_line = NULL;
    }
    printf("%d", amount);
}
