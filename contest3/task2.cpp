#include <iostream>
using namespace std;

struct Blank
{
    unsigned long ship_id;
    unsigned long run_id;
    unsigned long time_stamp;
    int event_type;
};
Blank x[10000], y[10000], z;

int main() {
    long N, count = 0, k = 0;
    cin >> N;
    for (long i = 0; i < N; i++) {
        Blank a;
        cin >> a.ship_id >> a.run_id >> a.time_stamp >> a.event_type;
        x[i] = a;
    }
    unsigned long id;
    cin >> id;
    for (int i = 0; i < N; i++) {
        if (x[i].ship_id == id) {
            y[count] = x[i];
            count += 1;
        }
    }
    for (int i = 0; i < count; i++) {
        for (int j = 0; j < count-1; j++) {
            if (y[j].time_stamp > y[j+1].time_stamp) {
                z = y[j];
                y[j] = y[j+1];
                y[j+1] = z;
            }
        }
    }
    bool flag = true;
    for (int j = 0; j < count; j++) {
        if (not(y[j].event_type == k)) {
            flag = false;
            cout << "NO";
            break;
        }
        k += 1;
        if (y[j].run_id != y[j+1].run_id) {
            k = 0;
        }
    }
    if (flag) {
        cout << "YES";
    }
    return 0;
}