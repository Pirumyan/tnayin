#include<stdio.h>
int main ()
{
	int numb1=0;
	int numb2=0;
		printf("Write 2 numbers you want to Compare\n");
		scanf(" %d%d",&numb1 ,&numb2);
	if (numb1>numb2)
		printf("%d>%d\n", numb1,numb2);
	else
		printf("%d>%d\n",numb2,numb1);


}
