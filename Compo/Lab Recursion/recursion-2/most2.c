#include <stdio.h>
int mostnum(int num, int arr[],int max, int i){
    if(i == num){
        return max;
    }
    if(arr[i] >= max){
        max = arr[i];
    }
    return mostnum(num,arr,max,i+1);
}

int main(){
    int num;
    printf("Input number:");
    scanf("%d",&num);

    int arr[num];
    for(int i = 0; i < num;i++){
        printf("input number in arr:");
        scanf("%d", &arr[i]);
    }
    // for(int i = 0; i < num;i++){
    //     printf("%d ", arr[i]);
    // }
    int max = mostnum(num,arr,arr[0],0);
    printf("%d", max);
    
    return 0;
}