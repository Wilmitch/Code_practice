#include <stdio.h>

int main(void)
{
    int speed = 50;
    int time = 5;

    printf("Enter the speed: \n");
    scanf("%d", &speed);

    printf("Enter the time: \n");
    scanf("%d", &time);
    
    int distance = speed * time;
    printf("The distance: %d\n", distance);
    return (0);
}