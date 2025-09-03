#include <stdio.h>
int main() {
    int score;
    scanf("%d", &score);
    if (score >= 80 && score <= 100) {
        printf("Grade A");
    }
    if (score >= 70 && score < 80) {
        printf("Grade B");
    }
    if (score >= 60 && score <70) {
        printf("Grade C");
    }
    if (score >= 50 && score <60) {
        printf("Grade D");
    }
    if (score >= 0 && score <50) {
        printf("Grade F");
    }
}