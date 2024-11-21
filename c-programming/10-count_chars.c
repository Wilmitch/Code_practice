#include <stdio.h>

int main(void)
{
    long nc;

    nc = 0;

    while (getchar() != EOF)
        ++nc;

    printf("The string has %ld character/s\n", nc);

    return(0);

}