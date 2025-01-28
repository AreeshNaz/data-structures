#include <stdio.h>
#define MAX 100

typedef struct {
    int arr[MAX];
    int top;
} Stack;

void initStack(Stack *s) {
    s->top = -1;
}

int isEmpty(Stack *s) {
    return s->top == -1;
}

void push(Stack *s, int data) {
    if (s->top == MAX - 1) return;
    s->arr[++(s->top)] = data;
}

int pop(Stack *s) {
    if (isEmpty(s)) return -1;
    return s->arr[(s->top)--];
}

int peek(Stack *s) {
    if (isEmpty(s)) return -1;
    return s->arr[s->top];
}

void addAtBottom(Stack *s, int data) {
    if (isEmpty(s)) {
        push(s, data);
        return;
    }
    int top = pop(s);
    addAtBottom(s, data);
    push(s, top);
}

void display(Stack *s, FILE *output) {
    for (int i = s->top; i >= 0; i--) {
        fprintf(output, "%d ", s->arr[i]);
    }
    fprintf(output, "\n");
}

int main() {
    Stack s;
    initStack(&s);

    FILE *input = fopen("input.txt", "r");
    FILE *output = fopen("output.txt", "w");

    if (input == NULL || output == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    int n, data;
    fscanf(input, "%d", &n);  // Read the number of elements to push

    for (int i = 0; i < n; i++) {
        fscanf(input, "%d", &data);
        push(&s, data);
    }

    fscanf(input, "%d", &data);  // Read the value to add at the bottom
    addAtBottom(&s, data);

    fprintf(output, "Stack After Adding %d at the Bottom:\n", data);
    display(&s, output);

    fclose(input);
    fclose(output);

    return 0;
}
