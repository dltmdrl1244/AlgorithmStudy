#include <bits/stdc++.h>
#define FASTIO cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);

using namespace std;

int getScore(int number)
{
    int cnt = 0;
    int t = 1;
    while (number > 0)
    {
        cnt += (number & 1);
        number >>= 1;
    }

    return cnt;
}

int main()
{  
    FASTIO;
    // freopen("input.txt", "r", stdin);
    int n, ans = 0;
    cin >> n;
    vector<int> arr(n+1);
    vector<int> dp(n+1, 0);

    for (int i = 1; i <= n; i++)
    {
        cin >> arr[i];
    }

    if (n == 1)
    {
        cout << 0 << endl;
        return 0;
    }
    
    dp[2] = getScore(arr[1] ^ arr[2]);
    dp[3] = getScore(arr[1] ^ arr[2] ^ arr[3]);
    dp[4] = dp[2] + getScore(arr[3] ^ arr[4]);

    for (int i = 5; i <= n; i++)
    {
        dp[i] = max(dp[i], dp[i-2] + getScore(arr[i-1] ^ arr[i]));
        dp[i] = max(dp[i], dp[i-3] + getScore(arr[i-2] ^ arr[i-1] ^ arr[i]));
    }
    cout << dp[n] << endl;
}