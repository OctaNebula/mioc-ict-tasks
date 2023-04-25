#include <cstdio>

int main () {
    int n;
    scanf("%d", &n);

    int i = 2;
    while (n % i)
        i++;

    printf("%d\n", i);
    return 0;
}
