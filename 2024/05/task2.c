#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct {
    long val;
    int outgoing;
    bool visited;
    int *adj;
} Node;

typedef struct {
    Node *nodes;
    int size;
} Digraph;

void safe_exit(Digraph *digraph, int code) {
    for (int i = 0; i < digraph->size; i++) {
        if (digraph->nodes[i].adj!= NULL) free(digraph->nodes[i].adj);
    }
    free(digraph->nodes);
    exit(code);
}

int get_key(Digraph digraph, long val) {
    if (!digraph.size) return -1;
    for (int i = 0; i < digraph.size; i++) {
        if (digraph.nodes[i].val == val) return i;
    }
    return -1;
}

int add_node(Digraph *digraph, Node node) {
    Node *new = realloc(digraph->nodes, ++(digraph->size) * sizeof(Node));
    if (new == NULL) {
        if (digraph->nodes != NULL) free(digraph->nodes);
        return -1;
    }
    digraph->nodes = new;
    digraph->nodes[digraph->size-1] = node;
    return digraph->size-1;
}


int add_adjacent(Node *node, int key) {
    for (int i = 0; i < node->outgoing; i++) {
#pragma clang diagnostic push
#pragma ide diagnostic ignored "NullDereference" // pointer known not to be null from size
        if (node->adj[i] == key) return 0;
#pragma clang diagnostic pop
    }
    int *new_adj = realloc(node->adj, ++(node->outgoing) * sizeof(int));
    if (new_adj == NULL) {
        if (node->adj == NULL) free(node->adj);
        return -1;
    }
    node->adj = new_adj;
    node->adj[node->outgoing-1] = key;
    return 0;
}

bool reachable(Digraph *digraph, long target_val, long start_val){
    Node *current = &(digraph->nodes[get_key(*digraph, start_val)]);
    for (int i = 0; i < current->outgoing; i++) {
        int key = current->adj[i];
        if (digraph->nodes[key].val == target_val) return true;
    }
    return false;
}

void swap(char *start, long *queue, int offset) {
    long first_int = *queue;
    *queue = *(queue+offset);
    *(queue+offset) = first_int;
    char first = *start, second = *(start+1);
    char *second_start = start + offset * 3;
    *start = *second_start;
    *(start+1) = *(second_start + 1);
    *second_start = first;
    *(second_start+1) = second;
}

int main(){
	FILE *input_file=fopen("input.txt", "r");
    Digraph digraph = {NULL, 0};
    char *line = NULL, *pos;
    size_t len;
    while (getline(&line, &len, input_file) != -1) {
        if (*line == '\n') break;
        pos = line;
        long first_val = strtol(pos, &pos, 10), second_val = strtol(pos+1, &pos, 10);
        int first_key = get_key(digraph, first_val), second_key = get_key(digraph, second_val);
        if (first_key == -1) {
            Node first_node = {first_val, 0, false, NULL};
            first_key = add_node(&digraph, first_node);
            if (first_key == -1) safe_exit(&digraph, -1);
        } if (second_key == -1) {
            Node second_node = {second_val, 0, false, NULL};
            second_key = add_node(&digraph, second_node);
            if (second_key == -1) safe_exit(&digraph, -1);
        }
        if (add_adjacent(&(digraph.nodes[first_key]), second_key) == -1) safe_exit(&digraph, -1);
    }
    long *queue = malloc(0);
    long result = 0;
    size_t counter = getline(&line, &len, input_file);
    do {
        size_t num_pages = counter / 3;
        long* new_queue = realloc(queue, num_pages * sizeof(long));
        if (new_queue == NULL) {
            free(queue);
            safe_exit(&digraph, -1);
        }
        queue = new_queue;
        bool swapped = false;
        int i = 0;
        for (; i < num_pages; i++) {
            *(queue+i) = strtol(line + 3*i, NULL, 10);
            int j = 0;
            for (; j < i; j++) {
                if (reachable(&digraph, *(queue+j), *(queue+i))) {
                    swap(line+j*3, queue+j, (i-j));
                    i = 0;
                    swapped = true;
                }
            }
        }
        if (swapped) {
            long middle = strtol(line + (counter / (3 * 2) * 3), NULL, 10);
            result += middle;
        }
        counter = getline(&line, &len, input_file);
    } while (counter != -1);
    printf("%ld", result);
    free(queue);
    safe_exit(&digraph, 0);
}
