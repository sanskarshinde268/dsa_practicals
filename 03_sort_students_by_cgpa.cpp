#include <iostream>
#include <string>
using namespace std;

struct Student { int id; string name; float cgpa; };

int main() {
    int n;
    cout << "Enter number of students: ";
    cin >> n;
    if (n <= 0) { cout << "Invalid size.\n"; return 0; }
    Student* s = new Student[n];

    for (int i = 0; i < n; i++) {
        cout << "Enter ID, name (one word), CGPA: ";
        cin >> s[i].id >> s[i].name >> s[i].cgpa;
    }

    // Bubble sort in ascending CGPA order
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (s[j].cgpa > s[j + 1].cgpa) {
                Student temp = s[j]; s[j] = s[j + 1]; s[j + 1] = temp;
            }

    cout << "\nStudents sorted by CGPA (ascending):\n";
    for (int i = 0; i < n; i++)
        cout << s[i].id << " " << s[i].name << " " << s[i].cgpa << '\n';
    delete[] s;
    return 0;
}