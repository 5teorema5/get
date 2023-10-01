#include <iostream>
#include <math.h>
using namespace std;

struct Blank
{
    unsigned long time_stamp;
    unsigned long id;
    float neural_activity;
};
struct Neurval
{
    unsigned long id;
    float neural_activity_max;
    float neural_activity_min;
};
Blank x[10000], z;
Neurval n[10000];

int main() {
    long N, max_id = 0, l=0, count = 1;
    float trash1, trash2, trash3, trash4;
    float n_max = 0, n_min = 100, neur_max, raz = 100.0;
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
        if (x[j].id == x[j+1].id) {
            count += 1;
            if (x[j].neural_activity > n_max) {
                n_max = x[j].neural_activity;
            }
            if (x[j+1].neural_activity > n_max) {
                n_max = x[j+1].neural_activity;
            }
            if (x[j].neural_activity < n_min) {
                n_min = x[j].neural_activity;
            }
            if (x[j+1].neural_activity < n_min) {
                n_min = x[j+1].neural_activity;
            }
        }
        else {
            if (count > 1) {
                n[l].id = x[j].id;
                n[l].neural_activity_max = n_max;
                n[l].neural_activity_min = n_min;
                l += 1;
                
            }
            n_max = 0.0;
            n_min = 100.0;
            count = 1; 
        }
    }
    for (int i = 0; i < l; i++) {
        if (n[i].neural_activity_max - n[i].neural_activity_min >= 0) {
            if (n[i].neural_activity_max - n[i].neural_activity_min < raz) {
                raz = n[i].neural_activity_max - n[i].neural_activity_min;
                neur_max = n[i].neural_activity_max;
                max_id = n[i].id;
            }
            if (n[i].neural_activity_max - n[i].neural_activity_min == raz) {
                if (n[i].neural_activity_max > neur_max) {
                    neur_max = n[i].neural_activity_max;
                    max_id = n[i].id;
                }
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