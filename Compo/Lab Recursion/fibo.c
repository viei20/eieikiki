#include <stdio.h>
int fibo(int num) {
    if(num == 0){
        return 0;
    }
    if(num == 1){
        return 1;
    }
    return fibo(num-1) + fibo(num-2);
    
}
int main(){
    int num;
    printf("Number:");
    scanf("%d", &num);
    for(int i = 0; i<num;i++){
        printf("%d ", fibo(i));
    }
    
}