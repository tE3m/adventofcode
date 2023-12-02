# include "stdio.h"
# include "string.h"
#include "stdlib.h"


int main(){
    FILE *input_file = fopen("input.txt", "r");
    static char* colors[] = {"red", "green", "blue"};
    int possible_ids = 0;
    char line[200];
    while (fgets(line, 200, input_file) != NULL){
        int max[] = {0, 0, 0};
        char *cubes, *cubes_saveptr, *game_saveptr;
        char *game_str = strtok_r(line, ":", &cubes_saveptr);
        int game_id = strtol(game_str + 5, NULL, 10);
        do {
            cubes = strtok_r(NULL, ";", &cubes_saveptr);
            char cubes_copy[strlen(cubes)+1];
            strcpy(cubes_copy, cubes);
            char* color_ptr = strtok_r(cubes_copy, ",", &game_saveptr);
            while (color_ptr){
                int color;
                for (int i=0; i<3; i++){
                    if (strstr(color_ptr, colors[i])){
                        color = i;
                        break;
                    }
                }
                int amount = strtol(color_ptr, NULL, 10);
                max[color] = amount > max[color] ? amount : max[color];
                color_ptr = strtok_r(NULL, ",", &game_saveptr);
            }
        } while (strcmp(&cubes[(int) strlen(cubes)-1], "\n") != 0);
        possible_ids += max[0] <= 12 && max[1] <= 13 && max[2] <= 14 ? game_id : 0;
    }
    printf("%d", possible_ids);
    return 0;
}