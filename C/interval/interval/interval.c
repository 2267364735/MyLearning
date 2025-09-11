#include <stdio.h>

int main() {
	int hours1, minutes1, hours2, minutes2;

	scanf_s("%d %d %d %d", &hours1, &minutes1, &hours2, &minutes2);
	int ih = hours2 - hours1;
	int im = minutes2 - minutes1;
	if(im < 0) {
		im += 60;
		ih --;
	}
	printf("时间差是 %d 小时 %d 分钟\n", ih, im);
	return 0;
}