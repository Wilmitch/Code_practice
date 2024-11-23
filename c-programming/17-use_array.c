#include <stdio.h>
/***
 * write a program to count the number of occurrences of each digit, of white space 
 * characters (blank, tab, newline), and of all other characters.
 */
int main(void)
{
    int c, i, space, others;
    int nums[10];

    space = others = 0;
    for (i = 0; i < 10; i++)
    {
        nums[i] = 0;
    }
    while ((c = getchar()) != EOF)
    {
        if (c >= '0' && c <= '9')
            ++nums[c - '0'];
        else if (c == ' ' || c == '\n' || c == '\t')
            ++space;
        else
            ++others;
    }
    printf("The digits are:");
    for (i = 0; i < 10; i++)
        printf(" %d", nums[i]);

    printf(", there are %d spaces and %d other characters\n", space, others);

    return (0);
}