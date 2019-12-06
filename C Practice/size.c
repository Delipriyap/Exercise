#include<stdio.h> 
int main() 
{ 
   int a; 
   char *x; 
   x = (char *) &a; 
   a = 256; 
   x[0] = 4; 
   x[1] = 2; 
   printf("%dn",a);   
   return 0; 
}
