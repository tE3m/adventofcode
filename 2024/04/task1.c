#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

bool is_xmas(char first_char, char second_char, char third_char, char fourth_char) {
    return first_char == 'X' && second_char == 'M' && third_char == 'A' && fourth_char == 'S' ||
           first_char == 'S' && second_char == 'A' && third_char == 'M' && fourth_char == 'X';
}


int main() {
    FILE *input_file = fopen("input.txt", "r");
    char *first_line, *second_line, *third_line, *fourth_line;
    size_t len, remaining = 4;
    int offset, amount = 0;
    getline(&second_line, &len, input_file);
    getline(&third_line, &len, input_file);
    getline(&fourth_line, &len, input_file);
    do {
        first_line = second_line;
        second_line = third_line;
        third_line = fourth_line;
        fourth_line = NULL;
        remaining = remaining > 3 ? (getline(&fourth_line, &len, input_file) != -1) + 3 : remaining - 1;
        for (offset = 0; *(first_line+offset) != '\n'; offset++) {
            if (offset < len - 3)
                amount += is_xmas(*(first_line + offset), *(first_line + offset + 1), *(first_line + offset + 2),
                                  *(first_line + offset + 3));
            if (remaining > 3) {
                amount += is_xmas(*(first_line + offset), *(second_line + offset), *(third_line + offset),
                                  *(fourth_line + offset));
                if (offset >= 3)
                    amount += is_xmas(*(first_line + offset), *(second_line + offset - 1), *(third_line + offset - 2),
                                      *(fourth_line + offset - 3));
                if (offset < len - 3)
                    amount += is_xmas(*(first_line + offset), *(second_line + offset + 1), *(third_line + offset + 2),
                                      *(fourth_line + offset + 3));
            }
        }
        free(first_line);
    } while (remaining > 0);
    printf("%d", amount);
}
