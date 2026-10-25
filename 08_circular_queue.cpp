#include <iostream>
using namespace std;

const int SIZE = 5;
int q[SIZE], frontIndex = -1, rearIndex = -1;

bool isEmpty() { return frontIndex == -1; }
bool isFull() { return (rearIndex + 1) % SIZE == frontIndex; }

void enqueue(int value) {
    if (isFull()) { cout << "Queue is full.\n"; return; }
    if (isEmpty()) frontIndex = rearIndex = 0;
    else rearIndex = (rearIndex + 1) % SIZE;
    q[rearIndex] = value;
    cout << value << " enqueued.\n";
}
void dequeue() {
    if (isEmpty()) { cout << "Queue is empty.\n"; return; }
    cout << "Dequeued: " << q[frontIndex] << '\n';
    if (frontIndex == rearIndex) frontIndex = rearIndex = -1;
    else frontIndex = (frontIndex + 1) % SIZE;
}
void display() {
    if (isEmpty()) { cout << "Queue is empty.\n"; return; }
    cout << "Queue: ";
    int i = frontIndex;
    while (true) {
        cout << q[i] << " ";
        if (i == rearIndex) break;
        i = (i + 1) % SIZE;
    }
    cout << '\n';
}
int main() {
    int choice, value;
    do {
        cout << "\n1.Enqueue  2.Dequeue  3.Display  0.Exit\nChoice: ";
        cin >> choice;
        switch (choice) {
            case 1: cout << "Value: "; cin >> value; enqueue(value); break;
            case 2: dequeue(); break;
            case 3: display(); break;
            case 0: break;
            default: cout << "Invalid choice.\n";
        }
    } while (choice != 0);
    return 0;
}