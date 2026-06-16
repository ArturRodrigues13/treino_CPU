#include <iostream>
using namespace std;

int main() {

	int n1, n2, v, soma1 = 0, soma2 = 0;

	cin >> n1;
	for(int i = 0; i < n1; i ++) {
		cin >> v; soma1 += v;
	}

	cin >> n2;
	for(int i = 0; i < n2; i ++) {
		cin >> v; soma2 += v;
	}

	if(soma1 == soma2) cout << "OK" << endl;
		else if (soma1 > soma2)
			cout << "E > D: " << soma1 - soma2 << " kg" << endl;
		else
			cout << "D > E: " << soma2 - soma1 << " kg" << endl;

	return 0;
}
