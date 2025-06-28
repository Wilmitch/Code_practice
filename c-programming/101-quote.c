#include <unistd.h>
/**
 * main - entry point
 * Return: 1 on success
 */
int main(void)
{
    char str[] = "and that piece of art is useful\" - Dora Korpar, 2015-10-19";

    int i, len;
    i = 0;
    len = 0;

    while (str[i++] != '\0')
       len++;
    write(2, str, len);
    return (1);
}