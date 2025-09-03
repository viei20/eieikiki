#include <stdio.h>
int main() {
    int num;
    scanf("%d", &num);

    switch (num)
    {
    case 1:
        printf("You choose Option %d", num);
        break;
    case 2:
        printf("You choose Option %d", num);
        break;
    case 3:
        printf("You choose Option %d", num);
    default:
        printf("Invalid choice");
        break;
    }
}
