#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cout << "Enter number of student IDs: ";
    cin >> n;
    if (n <= 0) { cout << "Invalid size.\n"; return 0; }

    int* ids = new int[n];
    cout << "Enter IDs: ";
    for (int i = 0; i < n; i++) cin >> ids[i];

    sort(ids, ids + n); // binary search requires sorted data
    cout << "Sorted IDs: ";
    for (int i = 0; i < n; i++) cout << ids[i] << " ";
    cout << "\nEnter ID to search: ";
    int key; cin >> key;

    int low = 0, high = n - 1, position = -1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (ids[mid] == key) { position = mid; break; }
        if (ids[mid] < key) low = mid + 1;
        else high = mid - 1;
    }

    if (position != -1) cout << "ID found at sorted index " << position << ".\n";
    else cout << "ID not found.\n";
    delete[] ids;
    return 0;
}