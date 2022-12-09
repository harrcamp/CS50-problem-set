#include <stdio.h>

void meow(int n);

int main(void)
{
    meow(3);
}

void meow(int n)
{
   for (int i = 0; i < n; i++)
   {
       printf("meow\n");
   }
}

// while loop declare variable outside loop
// int main(void)
// {
//     int i = 0;
//     while (i < 3)
//     {
//         printf("meow\n");
//         i++;
//     }
// }

// for loop declare variable inside loop
















