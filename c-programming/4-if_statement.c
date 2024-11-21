#include <stdio.h>

int main(void)
{
    int grade = 0;

    printf("Enter a Grade: \n");
    scanf("%d", &grade);

    if (grade >= 90) printf("A\n");
    else if (grade >= 80) printf("B\n");
    else if (grade >= 50) printf("Pass\n");
    else printf("Fail!\n");

    return (0);
}