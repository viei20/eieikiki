#include <stdio.h>
int main() {
    int num;
    scanf("%d", &num);
    for (int i=1; i<13; i++){
       printf("%d x %d = %d\n", num, i, num*i);
    }
}