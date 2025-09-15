# include <stdio.h>

/*int main() {
	int x;
	int n = 1;

	printf("请输入一个整数：");
	scanf_s("%d", &x);

	if (x > 999) {
		n = 4;
	}else if(x > 99) {
		n = 3;
	}
	else if (x > 9) {
		n = 2;
	}

	printf("n = %d\n", n);

	return 0;
}*/
/*
int main() {
	int x;
	int n = 0;

	scanf_s("%d", &x);

	n++;
	x /= 10;
	while (x > 0) {
		n++;
		x /= 10;
	}

	printf("n = %d\n", n);
	return 0;
}
*/
int main() {
	int x;
	scanf_s("%d", &x);
	int n = 0;
	do
	{
		n++;
		x /= 10;
	} while (x > 0);
	printf("n = %d\n", n);
	return 0;
}