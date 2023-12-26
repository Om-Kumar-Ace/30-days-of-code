#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void print_even_odd_characters(char *s) {
    int len = strlen(s);
    for (int i = 0; i < len; i += 2) {
        printf("%c", s[i]);  
    }
    printf(" ");
    for (int i = 1; i < len; i += 2) {
        printf("%c", s[i]); 
    }
    printf("\n");
}

int main() {
    int t;  
    scanf("%d", &t);
    char s[100];

    for (int i = 0; i < t; ++i) {
        scanf("%s", s);
        print_even_odd_characters(s);
    }

    return 0;
}
