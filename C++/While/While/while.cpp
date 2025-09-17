#include <iostream>
using namespace std;
#include <ctime>

//int main() {
//	int num = 0;
//
//	while (num < 10) {
//		cout << num << endl;
//		num++;
//	}
//
//
//
//	system("pause");
//
//	return 0;
//}
int main() {
	srand((unsigned int)time(NULL));
	int num = rand() % 100 + 1;
	cout << num << endl;
	
	int val = 0;
	cin >> val;

	while (val != num) {
		if (val < num) {
			cout << "Too low!" << endl;
		}
		else {
			cout << "Too high!" << endl;
		}
		cin >> val;
	}
	cout << "You guessed it!" << endl;
	system("pause");

	return 0;
}