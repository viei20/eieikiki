#include <stdio.h>
int sum(int num){
    if(num == 0){
        return 0;
    }
    return num%10 + sum(num/10);
}

int main(){
int num;
printf("Number:");
scanf("%d", &num);
printf("%d", sum(num));
}
