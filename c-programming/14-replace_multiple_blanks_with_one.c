#include <stdio.h>
/**
 * Exercise >> Write a program to copy its input to its output, replacing each string of one or
 *  more blanks by a single blank
 */
int main(void)
{
    int c;

    while ((c = getchar()) != EOF)
    {
        if (c == ' ')
        {
            while((c = getchar()) == ' ');
            putchar(' ');
            if (c == EOF)
                break;
        }
        putchar(c);
    }
    return (0);
}