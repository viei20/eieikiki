#include <stdio.h>
int main(){
    int num;
    scanf("%d", &num);
    if(num <2){
        printf("Error");
    }
    else{
        int arr[num];
        for(int i=0;i<num; i++){
            scanf("%d", &arr[i]);
        }
        int *pi = arr;
        int max1, max2;

        if(*pi > *(pi+1)){
            max1 = *pi;
            max2 = *(pi+1);
        }
        else{
            max1 = *(pi+1);
            max2 = *pi;
        }
        //move pointer to ตน.ที่ 3
        pi +=2;
        for(int i = 2; i<num; i++){
            
            if(*pi > max1){
                max2 = max1;
                max1 = *pi;

            }
            else if(*pi > max2){
               max2 = *pi;
            }
            pi+=1;
        }
        printf("Second Last is %d", max2);
    }

    return 0;
}