#include <stdlib.h>
#include <stdio.h>
#include <math.h>

typedef struct node {
    long value;
    size_t amount_children;
    struct node **children;
} node;

typedef struct {
    size_t amount_nodes;
    node **nodes;
} graph;


node **add_node(node **nodes, size_t *size, node *new) {
    node **new_nodes = reallocarray(nodes, ++(*size), sizeof(node *));
    if (new_nodes == 0) exit(-1);
    new_nodes[*size - 1] = new;
    return new_nodes;
}

node *create_or_get_node(graph *stones, long value) {
    for (int i = 0; i < stones->amount_nodes; i++) if (stones->nodes[i]->value == value) return stones->nodes[i];
    node *new_node = malloc(sizeof(node));
    new_node->value = value;
    new_node->amount_children = 0;
    new_node->children = malloc(0);
    stones->nodes = add_node(stones->nodes, &(stones->amount_nodes), new_node);
    return new_node;
}

node *create_or_get_child(graph *stones, node *parent, long value) {
    node *new_node = create_or_get_node(stones, value);
    parent->children = add_node(parent->children, &(parent->amount_children), new_node);
    return new_node;
}

long amount_stones(graph *stones, node *current_stone, int current_level) {
    if (!current_level) return 1;
    long current_val = current_stone->value;
    if (current_stone->amount_children == 0) {
        if (current_val == 0) create_or_get_child(stones, current_stone, 1);
        else {
            int digit_count = (int) log10(current_val) + 1;
            if (!(digit_count % 2)) {
                int half_digit_power = (int) pow(10, digit_count / 2);
                create_or_get_child(stones, current_stone, current_val / half_digit_power);
                create_or_get_child(stones, current_stone, current_val % half_digit_power);
            } else create_or_get_child(stones, current_stone, current_val * 2024);
        }
    }
    long amount = 0;
    for (int i = 0; i < current_stone->amount_children; i++)
        amount += amount_stones(stones, current_stone->children[i], current_level - 1);
    return amount;
}

int main() {
    FILE *input_file = fopen("input.txt", "r");
    char *line = NULL;
    size_t size, len;
    len = getline(&line, &size, input_file);
    fclose(input_file);
    char *pos = line;
    graph *stones = malloc(sizeof(graph));
    stones->amount_nodes = 0;
    stones->nodes = malloc(0);
    long amount = 0;
    while (pos < line + len - 1) {
        amount += amount_stones(stones, create_or_get_node(stones, strtol(pos, &pos, 10)), 75);
        printf("%ld, %ld\n", amount, stones->amount_nodes);
        fflush(stdout);
        for (int i = 0; i < stones->amount_nodes; i++)
            for (int j = 0; j < stones->amount_nodes; j++)
                if (i != j && stones->nodes[i]->value == stones->nodes[j]->value) {
                    printf("%ld", stones->nodes[j]->value);
                }
    }
    free(line);
}
