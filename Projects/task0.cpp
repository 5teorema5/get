#include <iostream>

using namespace std;

void Binary(unsigned int n) {
    int x[32] = {0};
    for (int i = 0; i < 32; i++) {
        x[i] = (n - ((n >> 1) << 1 ));
        n = n >> 1;
    }
    for (int i = 31; i > 0; i--) {
        cout << x[i];
    }
    cout << '\n';
}

int main() {
    // ios_base::sync_with_stdio(false);
    // cin.tie(NULL);
    // cout.tie(NULL);
    int n;
    cin >> n;
    Binary(n);
    return 0;
}