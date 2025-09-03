#include <stdio.h>
int main(){
    int number;
    scanf("%d", &number);

    int i = number;
    while(i>0){
        printf("%d\n", i);
        i--;
    }
}