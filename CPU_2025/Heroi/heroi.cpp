#include <iostream>
#include <string>
using namespace std;

int main () {

	string nome;
	char c;

	cin >> nome;
	c = nome[0];

	while(cin >> nome) {
		if(nome[0] != c) {
			cout << "Bah!" << endl;
			return 1;
		}
	}

	cout << "Viva!" << endl;
	return 0;
}
