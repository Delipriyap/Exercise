#include<stdio.h>
struct Point {
  int x;
  int y;
};

int main()
{
  struct Point p1 = {10, 20};
  struct Point p2 = p1;
  printf("%p\n",&p1);
  printf("%p\n",&p2);
/*  if (p1 == p2)
   {
    printf("p1 and p2 are same ");
   }
  getchar();*/
  return 0;
}
