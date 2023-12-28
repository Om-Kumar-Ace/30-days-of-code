#include <stdio.h>
#include <string.h>

struct PhoneBookEntry {
    char name[100];
    char phone_number[15];
};

int main() {
    int n;
    scanf("%d", &n);

    struct PhoneBookEntry phone_book[n];

    for (int i = 0; i < n; i++) {
        scanf("%s %s", phone_book[i].name, phone_book[i].phone_number);
    }

    char query[100];
    while (scanf("%s", query) != EOF) {
        int found = 0;
        for (int i = 0; i < n; i++) {
            if (strcmp(query, phone_book[i].name) == 0) {
                printf("%s=%s\n", query, phone_book[i].phone_number);
                found = 1;
                break;
            }
        }

        if (!found) {
            printf("Not found\n");
        }
    }

    return 0;
}
