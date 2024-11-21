#include <stdio.h>

int main(void)
{
    float x = 0.8;
    double y = -9.2;

    printf("Enter x: ");
    scanf("%f", &x);

    printf("Enter y: ");
    scanf("%lf", &y);

    printf("x is: %f\n", x);
    printf("y is: %lf\n", y);
    return 0;
}