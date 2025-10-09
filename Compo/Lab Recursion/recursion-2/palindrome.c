#include <stdio.h>
#include <string.h>

int palindrome(char * text,int i, int len){
    if(i >= len){
        return 1;
    }
    if(text[i] == text[len]){
        return palindrome(text,i+1,len-1);
    }
    else{
        return 0;
    }
}

int main(){
    char text[1000];
    scanf("%s",text);
    printf("%s", text);
    int len = strlen(text);
    // printf("%d", len);

    if(palindrome(text, 0 ,len-1)){
        printf("Palindrome\n");
    }
    else{
        printf("Not Palindrome");
    }
    return 0;
}