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
	printf("ʱ����� %d Сʱ %d ����\n", ih, im);
	return 0;
}