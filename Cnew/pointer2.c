#include <stdio.h>
int main(){
    int num;
    scanf("%d", &num);

//keep value in arr
    int arr[num];
    for(int i=0; i <num; i++){
        scanf("%d",&arr[i]);
    }
//Create sum
    int sum = 0;
    int *pi = arr;
    // pi = arr;
    for(int i=0; i <num; i++){
        sum += *pi;
        pi+= 1;
    }

    printf("Sum is %d", sum);


    return 0;

    
}