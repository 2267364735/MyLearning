#include <stdio.h>

int main() {
	int price = 0;
	int bill = 0;
	// 读入金额和票面
	printf("请输入金额：");
	scanf_s("%d", &price);
	printf("请输入票面：");
	scanf_s("%d", &bill);
	// 计算找零
	if (bill < price) {
		printf("票面不足，无法支付！\n");
	} else if (bill == price) {
		printf("金额刚好，无需找零！\n");
	} else {
		int change = bill - price;
		printf("找零金额：%d\n", change);
	}
	return 0;
}