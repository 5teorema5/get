#include <iostream>
using namespace std;

struct data()
{
    /* data */
};


int main() {
    long N, x[4][10000] = {{0}}, y[4][10000] = {{0}}, id, z[4] = {0};
    cin >> N;
    for (long i = 0; i < N; i++) {
        cin >> x[0][i] >> x[1][i] >> x[2][i] >> x[3][i];
    }
    cin >> id;
    for (long i = 0; i < N; i++) {
        if (id == x[0][i]) {
            y[0][i] = x[0][i];
            y[1][i] = x[1][i];
            y[2][i] = x[2][i];
            y[3][i] = x[3][i];
        }
    }
    for (int i = 0; i < N; i ++) {
        for (int j = 0; j < N-1; j++) {
            if (x[2][i] > x[2][i+1]) {
                z[0] = x[0][i];
                z[1] = x[1][i];
                z[2] = x[2][i];
                z[3] = x[3][i];
                x[0][i] = 
            }
        }
    }
    
    for (long i = 0; i < N; i++) {
        cout << y[0][i] << " " << y[1][i] << ' ' << y[2][i] << ' ' << y[3][i];
    }
    return 0;
}