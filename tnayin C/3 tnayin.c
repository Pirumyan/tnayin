#include<stdio.h>
int main ()
{
	int a= 0;
	int b= 0;
	int c= 0;
		printf("Wriet 3 numbers \n");
		scanf(" %d%d%d", &a, &b, &c);
	if (a==b&&c>a)
		printf("The biggist number -%d\n",c);
	else if(a==c&&b>a)
		printf("The biggist number-%d\n",b);
	else if (b==c&&a>b)
		printf("The biggest number - %d\n",a);
	else
		printf("There are different numbers - %d,%d,%d\n",a,b,c);





}
