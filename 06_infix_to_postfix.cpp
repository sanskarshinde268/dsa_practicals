#include <iostream>
#include <stack>
#include <string>
#include <cctype>
using namespace std;

int precedence(char op) {
    if (op == '^') return 3;
    if (op == '*' || op == '/' || op == '%') return 2;
    if (op == '+' || op == '-') return 1;
    return 0;
}
int main() {
    string infix, postfix;
    cout << "Enter infix expression (single-letter/digit operands, no spaces): ";
    cin >> infix;
    stack<char> st;

    for (char ch : infix) {
        if (isalnum(static_cast<unsigned char>(ch))) postfix += ch;
        else if (ch == '(') st.push(ch);
        else if (ch == ')') {
            while (!st.empty() && st.top() != '(') { postfix += st.top(); st.pop(); }
            if (!st.empty()) st.pop();
        } else {
            while (!st.empty() && st.top() != '(' &&
                   (precedence(st.top()) > precedence(ch) ||
                   (precedence(st.top()) == precedence(ch) && ch != '^'))) {
                postfix += st.top(); st.pop();
            }
            st.push(ch);
        }
    }
    while (!st.empty()) { if (st.top() != '(') postfix += st.top(); st.pop(); }
    cout << "Postfix: " << postfix << '\n';
    return 0;
}