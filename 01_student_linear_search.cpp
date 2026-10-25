#include <iostream>
#include <string>
using namespace std;

struct Student {
    int id;
    string name;
    float cgpa;
};

int main() {
    int n;
    cout << "Enter number of students: ";
    cin >> n;
    if (n <= 0) { cout << "Invalid number of students.\n"; return 0; }

    Student* students = new Student[n]; // dynamic memory allocation
    for (int i = 0; i < n; i++) {
        cout << "Enter ID, name (one word), CGPA for student " << i + 1 << ": ";
        cin >> students[i].id >> students[i].name >> students[i].cgpa;
    }

    int key;
    cout << "Enter student ID to search: ";
    cin >> key;
    int found = -1;
    for (int i = 0; i < n; i++) {
        if (students[i].id == key) { found = i; break; }
    }

    if (found != -1)
        cout << "Found: ID=" << students[found].id << ", Name=" << students[found].name
             << ", CGPA=" << students[found].cgpa << '\n';
    else cout << "Student not found.\n";

    delete[] students;
    return 0;
}
