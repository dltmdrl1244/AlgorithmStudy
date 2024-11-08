#include <bits/stdc++.h>
#define FASTIO cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
using namespace std;

int main()
{  
    FASTIO;
    // freopen("input.txt", "r", stdin);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int t, count = 0;
        int arr[1001];
        cin >> t;
        for (int j = 0; j < t; j++)
        {
            cin >> arr[j];
        }
        
        for (int j = 0; j < t; j++)
        {
            for (int k = 0; k < t - 1; k++)
            {
                if (arr[k] > arr[k+1])
                {
                    int temp;
                    temp = arr[k];
                    arr[k] = arr[k+1];
                    arr[k+1] = temp;
                    count++;
                }
            }
        }
        cout << count << endl;
    }
    
}