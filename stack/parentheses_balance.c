#include <stdio.h>
#include <stdlib.h>

#define MAX 100

typedef struct {
    char arr[MAX];
    int top;
} Stack;

void initStack(Stack *s) {
    s->top = -1;
}

int isEmpty(Stack *s) {
    return s->top == -1;
}

void push(Stack *s, char data) {
    if (s->top == MAX - 1) {
        printf("Stack Overflow\n");
        return;
    }
    s->arr[++(s->top)] = data;
}

char pop(Stack *s) {
    if (isEmpty(s)) {
        return '\0';
    }
    return s->arr[(s->top)--];
}

int isMatching(char open, char close) {
    return (open == '(' && close == ')') ||
           (open == '[' && close == ']') ||
           (open == '{' && close == '}');
}

int isBalanced(char* equation) {
    Stack stack;
    initStack(&stack);

    for (int i = 0; equation[i] != '\0'; i++) {
        char ch = equation[i];
        if (ch == '(' || ch == '[' || ch == '{') {
            push(&stack, ch);
        } else if (ch == ')' || ch == ']' || ch == '}') {
            if (isEmpty(&stack) || !isMatching(pop(&stack), ch)) {
                return 0;
            }
        }
    }
    return isEmpty(&stack);
}

int main() {
    char equation1[] = "((3^2 + 8) *(5/2))/(2+6)";
    char equation2[] = "((32 + 8) * (5/2) ) / (2+6))";
    char equation3[] = ")()())(";

    printf("((3^2 + 8) *(5/2))/(2+6) Equation is balanced? %s\n", isBalanced(equation1) ? "Yes" : "No");
    printf("((32 + 8) * (5/2) ) / (2+6)) Equation is balanced? %s\n", isBalanced(equation2) ? "Yes" : "No");
    printf(")()())( Equation is balanced? %s\n", isBalanced(equation3) ? "Yes" : "No");

    return 0;
}
