#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Log {
    Log() = default;
    Log(long shipId, long runId, long timeStamp, int eventType): shipId(shipId), runId(runId), timeStamp(timeStamp), eventType(eventType) {}
    long shipId;
    long runId;
    long timeStamp;
    int eventType;
};

// bool Check(long sId, long rId, long tStamp, int eType, Log log) {
//     if (tStamp > log.timeStamp && eType <= log.eventType) {
//         return false;
//     } else if (eType == 0 && log.eventType != 3) {
//         return false;
//     } {

//     }
// }

bool compare(Log a, Log b) {
    return a.timeStamp < b.timeStamp;
}

int main() {
    long N;

    cin >> N;

    long sId, rId, tStamp;
    int eType;

    vector<Log> log;
    vector<Log> logCheck;

    bool isOk = true;

    long search;

    for (int i = 0; i < N; i++) {
        cin >> sId >> rId >> tStamp >> eType;

        Log newLog;
        newLog.shipId = sId;
        newLog.runId = rId;
        newLog.timeStamp = tStamp;
        newLog.eventType = eType;
            
        log.push_back(newLog);
    }

    cin >> search;

    for (int i = 0; i < log.size(); i++) {
        if (log[i].shipId == search) {
            logCheck.push_back(log[i]);
        }
    }

    sort(logCheck.begin(), logCheck.end(), compare);

    bool flag = false;

    for (int  i = 0; i < logCheck.size() - 1; i++) {
        if (logCheck[i].eventType != 3 && logCheck[i].eventType >= logCheck[i + 1].eventType) {
            flag = true;

            break;
        }
    }

    if (flag) {
        cout << "NO\n";
    } else {
        cout << "YES\n";
    }

    // for (int i = 0; i < logCheck.size(); i++) {
    //     cout << logCheck[i].shipId << ' '
    //         << logCheck[i].runId << ' '
    //         << logCheck[i].timeStamp << ' '
    //         << logCheck[i].eventType << "\n";
    // }

    return 0;
}