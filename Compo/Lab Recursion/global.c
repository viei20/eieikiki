#include <stdio.h>
int factorial(int num){
   if(num == 0){
    return 1;
   }
   return num * factorial(num-1);
}

int main(){
    int num;
    printf("Number:");
    scanf("%d",&num);
    factorial(num);
    printf("%d", factorial(num));
    return 0;
}