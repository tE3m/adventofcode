# include "stdio.h"
# include "ctype.h"
# include "stdlib.h"

int* normalize(int value){
    int *result = malloc(2*sizeof(int));
    result[1] = value % 10;
    if (value)
    while (value > 10){
        value /= 10;
    }
    result[0] = value;
    return result;
}

int main(void){
    FILE *input_file = fopen("./input.txt", "r");
    int result=0, firstValue, secondValue;
    char line[100];
    while (fgets(line, 100, input_file) != NULL){;
        char *p = line;
        firstValue = 0, secondValue = 0;
        while (*p){
            if (isdigit(*p)){
                if (firstValue == 0 && secondValue != 0){
                    if (secondValue > 9){
                        int* values = normalize(secondValue);
                        firstValue = values[0];
                        free(values);
                    } else {
                        firstValue = secondValue;
                    }
                }
                secondValue = strtol(p, &p,10);
            }
            p++;
        }
        if (firstValue && secondValue > 9){
            secondValue = normalize(secondValue)[1];
        } else if (secondValue > 99) {
            int *values = normalize(secondValue);
            firstValue = values[0];
            secondValue = values[1];
            free(values);
        } else if (!firstValue && secondValue < 10) {
            firstValue = secondValue;
        }
        result += firstValue * 10 + secondValue;
    }
    fclose(input_file);
    printf("%d", result);
    return 0;
}