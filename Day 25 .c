#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int t;
    scanf("%d", &t);
    int n;
    for(int i = 0 ; i < t ; i++){
        scanf("%d", &n);
        if((n % 2 == 0 && n != 2) || n == 1){
            printf("Not prime\n");
        }
        else{
            int isPrime = 1;
            for(int i = 3 ; i <= n/2 ; i+=2){
                if(n % i == 0){
                    isPrime = 0;
                    break;
                }
            } 
            if(isPrime)
                printf("Prime\n");
            else
                printf("Not prime\n");
        }
    }
}
