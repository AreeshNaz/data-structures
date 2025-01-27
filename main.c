#include <stdio.h>
#define N 5
int stack[N];
int top=-1;
void push(int x){
    if(top== N-1){
        printf("Overflow");
    }
    else{
        top++;
        stack[top]=x;
      
    }
}
void pop(){
    int item;
    if(top==-1)
    {
        printf("Underflow");
    }
    else{
        item=stack[top];
        top--;
        printf("%d is pop ",item);
    }
}
void peek(){
    if(top==-1){
        printf("No element in the stack");
    }
    else{
        printf("%d", stack[top]);
    }
}
void display(){
    int i;
    for(i=top;i>=0;i--){
        printf("%d",stack[i]);
    }
}
int main(){
    push(8);
     push(7);
      push(6);
       push(9);
    
   // pop();
  // peek();
  display();
    return 0;
}
