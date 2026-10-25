#include <iostream>
using namespace std;

struct Node { int data; Node* next; };
Node* topNode = nullptr;

void push(int value) {
    Node* node = new Node{value, topNode};
    topNode = node;
    cout << value << " pushed.\n";
}
void pop() {
    if (!topNode) { cout << "Stack underflow: stack is empty.\n"; return; }
    Node* temp = topNode;
    cout << "Popped: " << temp->data << '\n';
    topNode = topNode->next;
    delete temp;
}
void display() {
    if (!topNode) { cout << "Stack is empty.\n"; return; }
    cout << "Stack (top to bottom): ";
    for (Node* p = topNode; p; p = p->next) cout << p->data << " ";
    cout << '\n';
}
int main() {
    int choice, value;
    do {
        cout << "\n1.Push  2.Pop  3.Display  0.Exit\nChoice: ";
        cin >> choice;
        switch (choice) {
            case 1: cout << "Value: "; cin >> value; push(value); break;
            case 2: pop(); break;
            case 3: display(); break;
            case 0: break;
            default: cout << "Invalid choice.\n";
        }
    } while (choice != 0);
    while (topNode) pop(); // free remaining nodes
    return 0;
}