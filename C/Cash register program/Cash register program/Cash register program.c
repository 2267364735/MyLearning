#include <stdio.h>

int main() {
	int price = 0;
	int bill = 0;
	// �������Ʊ��
	printf("�������");
	scanf_s("%d", &price);
	printf("������Ʊ�棺");
	scanf_s("%d", &bill);
	// ��������
	if (bill < price) {
		printf("Ʊ�治�㣬�޷�֧����\n");
	} else if (bill == price) {
		printf("���պã��������㣡\n");
	} else {
		int change = bill - price;
		printf("�����%d\n", change);
	}
	return 0;
}