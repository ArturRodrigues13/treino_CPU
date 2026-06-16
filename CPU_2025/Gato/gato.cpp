#include <iostream>
using namespace std;

int main() {

	int x1, x2, y1, y2, r;
	cin >> x1 >> y1 >> r;
	cin >> x2 >> y2;

	if((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) <= r * r)
		cout << "Gato" << endl;
	else
		cout << "Gaiato" << endl;

	return 0;
}
