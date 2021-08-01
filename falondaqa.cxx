#include<stdio.h>
int main()
{
  int rows=6;
  for(int i=0;i<rows;i++)
  {
    for(int j=rows-2;j>=i;j--)
    {
      printf("%c ",'E'-j);
    }
    for(int l=0;l<i;l++)
    {
      printf("    ");
    }
    for(int k=i;k<=rows-2;k++)
    {
      printf("%c ",'E'-k);
    }
    printf("\n");
  }
  return 0;
}