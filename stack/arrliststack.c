#include <stdio.h>
#include <stdlib.h>

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
    if (s->top == MAX - 1) {
        printf("Stack Overflow\n");
        return;
    }
    s->arr[++(s->top)] = data;
}

int pop(Stack *s) {
    if (isEmpty(s)) {
        return -1;
    }
    return s->arr[(s->top)--];
}

int peek(Stack *s) {
    if (isEmpty(s)) {
        return -1;
    }
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

void reverseStack(Stack *s) {
    if (isEmpty(s)) {
        return;
    }
    int top = pop(s);
    reverseStack(s);
    addAtBottom(s, top);
}

void display(Stack *s) {
    for (int i = s->top; i >= 0; i--) {
        printf("%d ", s->arr[i]);
    }
    printf("\n");
}

int main() {
    Stack s;
    initStack(&s);

    push(&s, 1);
    push(&s, 2);
    push(&s, 3);
    push(&s, 4);
    push(&s, 45);

    printf("Original Stack:\n");
    display(&s);

    addAtBottom(&s, 99);  // Adding 99 at the bottom
    reverseStack(&s);  // Reversing the stack

    printf("Stack After Adding 99 at the Bottom and Reversing:\n");
    display(&s);

    return 0;
}
