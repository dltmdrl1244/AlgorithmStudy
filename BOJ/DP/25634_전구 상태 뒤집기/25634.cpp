#include <bits/stdc++.h>
#define FASTIO cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
using namespace std;

int main()
{  
    FASTIO;
    freopen("input.txt", "r", stdin);
    
    int n, ans = 0;
    cin >> n;
    vector<int> arr(n), dp(n);

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
        dp[i] = -9999;
    }
    for (int i = 0; i < n; i++)
    {
        int a;
        cin >> a;
        if (a == 1)
        {
            ans += arr[i];
            arr[i] = -arr[i];
        }
    }

    dp[0] = arr[0];
    for (int i = 1; i < n; i++)
    {
        dp[i] = max(arr[i], dp[i-1] + arr[i]);
    }
    
    int maxVal = -9999;
    for (int i = 0; i < n; i++)
    {
        maxVal = max(maxVal, dp[i]);
    }

    cout << maxVal + ans << endl;
}