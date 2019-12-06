#include<stdio.h>
int main(void)
{
int a[10],i,j,temp;
printf("\nnumbers are");
for(i=0; i<10;i++)
	{
	scanf("\n%d",&a[i]);
	}	

for (i=0;i<10;i++)
	{
		for(j=0;j<10;j++)
		{	
	 	if (a[j]<a[i])
			{	
			temp=a[i];
			a[i]=a[j];
			a[j]=temp;
			}
		}

	}

for(i=0;i<10;i++)
{
printf("\n sorted numbers are%d\t",a[i]);
}

return 0;
}
