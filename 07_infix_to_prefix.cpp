#include <iostream>
#include <stack>
#include <string>
#include <algorithm>
#include <cctype>
using namespace std;

int prec(char c) {
    if (c == '^') return 3;
    if (c == '*' || c == '/' || c == '%') return 2;
    if (c == '+' || c == '-') return 1;
    return 0;
}
int main() {
    string infix;
    cout << "Enter infix expression (single-letter/digit operands, no spaces): ";
    cin >> infix;

    // Reverse, swap parentheses, convert to postfix, then reverse result.
    reverse(infix.begin(), infix.end());
    for (char &c : infix) {
        if (c == '(') c = ')';
        else if (c == ')') c = '(';
    }

    stack<char> st;
    string postfix;
    for (char c : infix) {
        if (isalnum(static_cast<unsigned char>(c))) postfix += c;
        else if (c == '(') st.push(c);
        else if (c == ')') {
            while (!st.empty() && st.top() != '(') { postfix += st.top(); st.pop(); }
            if (!st.empty()) st.pop();
        } else {
            // For reversed expression, equal precedence handling is reversed for right-associative ^.
            while (!st.empty() && st.top() != '(' &&
                   (prec(st.top()) > prec(c) ||
                   (prec(st.top()) == prec(c) && c == '^'))) {
                postfix += st.top(); st.pop();
            }
            st.push(c);
        }
    }
    while (!st.empty()) { if (st.top() != '(') postfix += st.top(); st.pop(); }
    reverse(postfix.begin(), postfix.end());
    cout << "Prefix: " << postfix << '\n';
    return 0;
}