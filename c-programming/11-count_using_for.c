#include <stdio.h>

int main(void)
{
    double nc;

    for (nc = 0; getchar() != EOF; ++nc)
    ;
    printf("The input has a total number of %.0f characters.\n", nc);

    return (0);
}