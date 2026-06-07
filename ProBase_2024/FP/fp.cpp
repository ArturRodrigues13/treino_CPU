#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    while (cin >> n) {
        vector<int> p(n+1,0);
        int sum = 0;
        for(int i = 1; i <= n; i++) {
            cin >> p[i];
            sum+=p[i];
        }
        int t = sum/2;
        int m[n+1][t+1];
        for(int i=0; i<=n; i++) m[i][0] = 0;
        for(int j=0; j<=t; j++) m[0][j] = 0;
        for(int i=1; i<=n; i++)
            for(int j=1; j<=t; j++) {
                m[i][j] = m[i-1][j];
                if(p[i] <= j && m[i-1][j-p[i]] + p[i] > m[i][j])
                    m[i][j] = m[i-1][j-p[i]] + p[i];
            }
        cout << (sum - t - m[n][t]) << endl;
    }
    return 0;
}
