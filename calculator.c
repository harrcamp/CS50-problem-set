#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x 
    long x = get_int("x: ");
    
    // Prompt user for y
    long y = get_int("y: ");
    
    // Perform addition
    long z = x + y;
    printf("%li\n", z);
}

