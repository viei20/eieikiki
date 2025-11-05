#include <stdio.h>
int main() {
    int a = 10;
    int *pa = &a;

    float b = 3.14;
    float *pb = &b;

    char c = 'A';
    char *pc = &c;

    printf("int %d: %p\nfloat %f:%p\nchar %c:%p\n",a,pa,b,pb,c,pc);
    return 0;
}