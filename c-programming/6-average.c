#include <stdio.h>

/*** The Define below is used to declare constants ***/
#define LOWER 0
#define UPPER 300
#define STEP 20

int main(void)
{
    int fahr;

    printf("Fahrenheit  Celsius\n");

    for (fahr = LOWER; fahr <= 300; fahr = fahr + STEP)
    {
        printf("%4d:\t%10.2f\n", fahr, 5.0/9.0 * (fahr - 32) / 9);
    }
    return (0);
}