#include <stdio.h>
#include <stdbool.h>
#include <string.h>
# include <stdlib.h>

// Implements a swap of element i and j in an array
void swap(int* a, const int i, const int j) {
    const int tmp = a[i];
    a[i] = a[j];
    a[j] = tmp;
}

int partition(int* a, const int lo, const int hi) {
    int i = lo, j = hi+1;
    int v = a[lo];
    while (true) {
        while (a[++i] < a[lo]) {
            if (i == hi) {
                break;
            }
        }
        while (a[lo] < a[--j]) {
            if (j == lo) {
                break;
            }
        }
        if (i >= j) {
            break;
        }
        swap(a, i, j);
    }
    swap(a, lo, j);
    return j;
}

// Implements quick sort
void quick_sort(int* a, const int lo, const int hi) {
    if (hi <= lo) {
        return;
    }
    int j = partition(a, lo, hi);
    quick_sort(a, lo, j-1);
    quick_sort(a, j+1, hi);
}

int main(){
    FILE *input_file=fopen("input.txt", "r");
    int left_column[1000], right_column[1000];
    char line[15];
    int sim = 0;
    for (int pos=0; fgets(line, 15, input_file) != NULL; pos++) {
        left_column[pos] = strtol(line, NULL, 10);
        right_column[pos] = strtol(line+5, NULL, 10);
    }
    quick_sort(right_column, 0, 999);
    for (int left_pos=0; left_pos<1000; left_pos++){
        int counter = 0;
        for (int right_pos=0; right_column[right_pos] <= left_column[left_pos]; right_pos++) {
            if (right_column[right_pos] == left_column[left_pos]) counter++;
        }
        sim += left_column[left_pos] * counter;
    }
    printf("Similarity is: %d", sim);
}