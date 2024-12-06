#include <stdlib.h>
#include <stdio.h>
#include <regex.h>

int main(){
	FILE *input_file=fopen("input_dont.txt", "r");
    regex_t expr;
    regmatch_t *pmatch = malloc(sizeof(regmatch_t)*3);
    regcomp(&expr, "mul\\(([[:digit:]]+),([[:digit:]]+)\\)", REG_EXTENDED);
    char *line = NULL, *pos = NULL;
    size_t len = 0;
    long sum = 0;
    while (getline(&line, &len, input_file) != -1) {
        pos = line;
        while (regexec(&expr, pos, 3, pmatch, 0) != REG_NOMATCH) {
            long first = strtol(pos+pmatch[1].rm_so, NULL, 10), second = strtol(pos+pmatch[2].rm_so, NULL, 10);
            sum += first * second;
            pos += pmatch[0].rm_eo;
        }
    }
    free(pmatch);
    printf("%ld", sum);
}
