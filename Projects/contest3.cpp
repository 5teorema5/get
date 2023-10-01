#include <iostream>
#include <math.h>
using namespace std;

struct Blank
{
    unsigned long time_stamp;
    unsigned long id;
    float neural_activity;
};
Blank x[10000], z;

int main() {
    long N, max_id = 0;
    float trash1, trash2, trash3, trash4;
    float max_activity = 0.0, raz = 100.0;
    cin >> N;
    for (long i = 0; i < N; i++){
        Blank a;
        cin >> a.time_stamp >> a.id >> trash1 >> trash2 >> trash3 >> a.neural_activity >> trash4;
        x[i] = a;
    }
    for (long i = 0; i < N; i++) {
        for (long j = 0; j < N-1; j++) {
            if (x[j].time_stamp > x[j+1].time_stamp) {
                z = x[j];
                x[j] = x[j+1];
                x[j+1] = z;
            }
        }
    }
    for (long i = 0; i < N; i++) {
        for (long j = 0; j < N-1; j++) {
            if (x[j].id > x[j+1].id) {
                z = x[j];
                x[j] = x[j+1];
                x[j+1] = z;
            }
        }
    }
    for (long j = 0; j < N; j++) {
        cout << x[j].time_stamp << ' ' << x[j].id << ' ' << x[j].neural_activity << '\n';
    }
    for (long j = 0; j < N-1; j++) {
        if (x[j].id == x[j+1].id) {
            if (fabs((x[j].neural_activity - x[j+1].neural_activity) <= raz) && 
            (max_activity < x[j].neural_activity)) {
                max_activity = x[j].neural_activity;
                max_id = x[j].id;
                raz = fabs(x[j].neural_activity - x[j+1].neural_activity);
            }
        }
    }
    if (max_id != 0) {
        cout << max_id;
    }
    else {
        cout << (-1);
    }
    return 0;
}