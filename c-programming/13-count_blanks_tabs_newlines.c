#include <stdio.h>
/**
 * This program prints the number of blanks, tabs and newlines that were inputed.
 */
int main(void)
{
    int n, c = 0, tab = 0, nl = 0, bl = 0;

    for (n = 0; (c = getchar()) != EOF; n++)
    {
        if (c == ' ')
            bl++;
        else if (c == '\t')
            tab++;
        else if (c == '\n')
            nl++;
    }
    printf("There is a total of %d newlines, %d blanks and %d tabs in that string\n", nl, bl, tab);

    return (0);
}   
