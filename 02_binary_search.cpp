
#include <iostream>
using namespace std;

int main()
{
    int n;

    cout << "Enter number of student IDs: ";
    cin >> n;

    if(n <= 0)
    {
        cout << "Invalid size.";
        return 0;
    }

    int* ids = new int[n];

    cout << "Enter IDs: ";
    for(int i = 0; i < n; i++)
    {
        cin >> ids[i];
    }

    // Bubble Sort
    for(int i = 0; i < n-1; i++)
    {
        for(int j = 0; j < n-i-1; j++)
        {
            if(ids[j] > ids[j+1])
            {
                int temp = ids[j];
                ids[j] = ids[j+1];
                ids[j+1] = temp;
            }
        }
    }

    // Display sorted IDs
    cout << "Sorted IDs: ";
    for(int i = 0; i < n; i++)
    {
        cout << ids[i] << " ";
    }

    // Binary Search
    int key;
    cout << "\nEnter ID to search: ";
    cin >> key;

    int low = 0, high = n-1, position = -1;

    while(low <= high)
    {
        int mid = (low + high) / 2;

        if(ids[mid] == key)
        {
            position = mid;
            break;
        }
        else if(ids[mid] < key)
        {
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }

    if(position != -1)
        cout << "ID found at index " << position;
    else
        cout << "ID not found.";

    delete[] ids;

    return 0;
}
